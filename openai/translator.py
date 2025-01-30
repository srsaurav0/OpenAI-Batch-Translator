import os
from dotenv import load_dotenv
import json
import time
from openai import OpenAI
from requests.exceptions import RequestException
from time import sleep

load_dotenv()
client = OpenAI(api_key=os.getenv("OpenAI_API_KEY"))


def prepare_batch_input(source_lang, target_lang, texts, filename="batchinput.jsonl"):
    """
    Prepare a .jsonl file with translation requests.

    Parameters:
    - source_lang: Source language code (e.g., 'en' for English).
    - target_lang: Target language code (e.g., 'fr' for French).
    - texts: List of texts to be translated.
    - filename: Output filename for the .jsonl file.

    Returns:
    - The filename of the generated batch input file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        for idx, text in enumerate(texts):
            request = {
                "custom_id": f"request-{idx}",
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": {
                    "model": "gpt-3.5-turbo",  # Choose appropriate model
                    "messages": [
                        {
                            "role": "system",
                            "content": f"Translate the sentence from {source_lang} to {target_lang}. \n"
                            "Keep all HTML tags, attributes, and links intact. \n"
                            "Keep all templates intact. \n"
                            "Translate only the visible text between the tags. \n"
                            'Do not change the string "Rent By Owner™" or "Rent by Owner". \n'
                            "Only output the translated sentence.",
                        },
                        {"role": "user", "content": text},
                    ],
                    "max_tokens": 5000,  # Adjust based on expected sentence length
                },
            }
            f.write(json.dumps(request) + "\n")

    return filename


def upload_batch_input(filename):
    """
    Upload the batch input file to OpenAI's servers.

    Parameters:
    - filename: The name of the batch input file to upload.

    Returns:
    - file_id: The ID of the uploaded file, used for creating the batch.
    """
    try:
        with open(filename, "rb") as f:
            file = client.files.create(file=f, purpose="batch")
        return file.id
    except RequestException as e:
        print(f"Error uploading file: {e}")
        return None


def create_batch(file_id, completion_window="24h"):
    """
    Create a batch job using the uploaded file.

    Parameters:
    - file_id: The ID of the uploaded file.
    - completion_window: The time window for batch completion.

    Returns:
    - batch_id: The ID of the created batch job.
    """
    try:
        batch = client.batches.create(
            input_file_id=file_id,
            endpoint="/v1/chat/completions",
            completion_window=completion_window,
        )
        return batch["id"]
    except RequestException as e:
        print(f"Error creating batch: {e}")
        return None


def check_batch_status(batch_id):
    """
    Check the status of a batch job.

    Parameters:
    - batch_id: The ID of the batch job to check.

    Returns:
    - batch_status: The status of the batch job.
    """
    try:
        batch = client.batches.retrieve(batch_id)
        return batch["status"]
    except RequestException as e:
        print(f"Error checking batch status: {e}")
        return "failed"


def retrieve_batch_results(batch_id):
    """
    Retrieve the results of a completed batch job.

    Parameters:
    - batch_id: The ID of the batch job.

    Returns:
    - results: The translated sentences.
    """
    try:
        batch = client.batches.retrieve(batch_id)
        output_file_id = batch["output_file_id"]

        # Download the output file
        file_response = client.files.content(output_file_id)
        file_contents = file_response.text()

        # Parse the output from the .jsonl file format
        results = []
        for line in file_contents.splitlines():
            result = json.loads(line)
            results.append(result["response"]["body"]["choices"][0]["message"]["content"])

        return results
    except RequestException as e:
        print(f"Error retrieving batch results: {e}")
        return []


def cancel_batch(batch_id):
    """
    Cancel a batch job.

    Parameters:
    - batch_id: The ID of the batch job to cancel.

    Returns:
    - batch: The updated batch object after cancellation.
    """
    try:
        batch = client.batches.cancel(batch_id)
        return batch
    except RequestException as e:
        print(f"Error cancelling batch: {e}")
        return None


def main():

    # Multiple lists of strings to translate
    texts_list_1 = [
        "RentByOwner.com offers a comprehensive online platform for travelers seeking the perfect vacation rental experience.",
        "With a wide selection of properties ranging from cozy holiday homes to luxurious villas, we cater to diverse travel needs and budgets.",
    ]

    texts_list_2 = [
        "Explore beautiful vacation homes across the world with RentByOwner.",
        "Our platform provides the best deals on villas, apartments, and vacation homes for your next getaway.",
    ]

    # More lists can be added as needed
    texts_lists = [texts_list_1, texts_list_2]

    source_lang = "en"  # Language code or language name
    target_lang = "es"  # Language code or language name

    batch_ids = []  # Store batch IDs for tracking

    # Step 1: Prepare and upload each batch in a loop
    for texts_to_translate in texts_lists:
        # Prepare the input file for each batch
        input_filename = prepare_batch_input(
            source_lang, target_lang, texts_to_translate
        )

        # Upload the input file
        file_id = upload_batch_input(input_filename)
        if not file_id:
            print("Skipping batch due to upload failure.")
            continue

        # Create the batch job for each batch
        batch_id = create_batch(file_id)
        if not batch_id:
            print("Skipping batch due to batch creation failure.")
            continue

        # Store the batch_id for future reference
        batch_ids.append(batch_id)

    # Step 2: Check the status of each batch in a loop
    all_batches_completed = False
    while not all_batches_completed:
        all_batches_completed = True  # Assume all batches are complete, check each
        for batch_id in batch_ids:
            batch_status = check_batch_status(batch_id)
            if batch_status != "completed":
                print(f"Batch {batch_id} is still processing...")
                all_batches_completed = False  # At least one batch is still processing
        if not all_batches_completed:
            print(
                "Some batches are still processing. Waiting for a minute before checking again."
            )
            time.sleep(60)  # Check again after a minute

    # Step 3: Once all batches are completed, retrieve the results for each batch
    for batch_id in batch_ids:
        translated_texts = retrieve_batch_results(batch_id)
        if translated_texts:
            print(f"Results for batch {batch_id}:")
            for translated_text in translated_texts:
                print(translated_text)
            print("\n")  # Add extra line between batch results


if __name__ == "__main__":
    main()

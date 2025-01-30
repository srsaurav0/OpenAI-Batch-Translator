import time

from batch_helpers.check_batch_status import check_batch_status
from batch_helpers.create_batch import create_batch
from batch_helpers.prepare_batch_input import prepare_batch_input
from batch_helpers.retrieve_batch_results import retrieve_batch_results
from batch_helpers.upload_batch_input import upload_batch_input


"""
Translates multiple lists of strings from a source language to a target language using OpenAI's Batch API.

This function processes a list of strings by dividing them into smaller batches, preparing the input files,
uploading them to OpenAI's server, and creating a batch job for each batch. It then monitors the batch job status,
waiting for all jobs to complete. Once completed, the function retrieves and prints the translation results.

Steps:
1. Prepares the translation input file for each batch (a .jsonl file).
2. Uploads the file to OpenAI's server for batch processing.
3. Creates a batch job for processing the translation.
4. Monitors the status of all batches to ensure they are completed.
5. Retrieves the results from the completed batches and prints them.

Parameters:
- source_lang (str): The source language code (e.g., 'en' for English).
- target_lang (str): The target language code (e.g., 'es' for Spanish).
- texts_lists (list of lists): A list containing multiple lists of strings to translate.

Returns:
None
"""


def translator():
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

import time
from batch_helpers.batch_inputs import get_text_lists
from batch_helpers.check_batch_status import check_batch_status
from batch_helpers.create_batch import create_batch
from batch_helpers.extract_content import extract_content_from_file
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

    texts_lists = get_text_lists()

    source_lang = "English"  # Language code or language name
    target_lang = "Spanish"  # Language code or language name

    batch_ids = []  # Store batch IDs for tracking
    file_ids = []

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

        file_ids.append(file_id)

        # Create the batch job for each batch
        batch_id = create_batch(file_id)
        if not batch_id:
            print("Skipping batch due to batch creation failure.")
            continue

        # Store the batch_id for future reference
        batch_ids.append(batch_id)

    print("Batch IDs:", batch_ids)
    print("File IDs:", file_ids)

    # Step 2: Check the status of each batch and handle them individually
    while batch_ids:
        for batch_id in batch_ids[
            :
        ]:  # Iterate over a copy of batch_ids to allow removal
            batch_status = check_batch_status(batch_id)

            if batch_status == "validating":
                print(f"Batch {batch_id} is being validated. Waiting...")

            elif batch_status == "failed":
                print(f"Batch {batch_id} failed validation. Removing from list.")
                batch_ids.remove(batch_id)

            elif batch_status == "in_progress":
                print(
                    f"Batch {batch_id} is currently being processed. Checking again later."
                )

            elif batch_status == "finalizing":
                print(f"Batch {batch_id} has completed and results are being prepared.")

            elif batch_status == "completed":
                print(f"Batch {batch_id} is completed. Retrieving results...")
                translated_texts = retrieve_batch_results(
                    batch_id, f"results/output_{batch_id}.jsonl"
                )

                if translated_texts:
                    output_filename = f"results/translated_results_{batch_id}.txt"
                    with open(output_filename, "w") as file:
                        for translated_text in translated_texts:
                            file.write(f"{translated_text}\n")
                    print(f"Results for batch {batch_id} saved to {output_filename}")
                    content_list = extract_content_from_file(output_filename, batch_id)
                    print(content_list)

                batch_ids.remove(batch_id)

            elif batch_status == "expired":
                print(
                    f"Batch {batch_id} expired. It was not completed within 24 hours. Removing from list."
                )
                batch_ids.remove(batch_id)

            elif batch_status == "cancelling":
                print(
                    f"Batch {batch_id} is being cancelled. Waiting for confirmation..."
                )

            elif batch_status == "cancelled":
                print(f"Batch {batch_id} was cancelled. Removing from list.")
                batch_ids.remove(batch_id)

            else:
                print(
                    f"Batch {batch_id} has an unknown status: {batch_status}. Investigating..."
                )

        # Wait before checking the status again for remaining batches
        if batch_ids:  # If there are still batches left to check
            time.sleep(60)  # Wait for a short period before checking again
        else:
            print("All batches are completed.")

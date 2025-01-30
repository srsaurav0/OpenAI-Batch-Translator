import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from requests.exceptions import RequestException

load_dotenv()
client = OpenAI(api_key=os.getenv("OpenAI_API_KEY"))


"""
Retrieve the results of a completed batch job.

Parameters:
- batch_id: The ID of the batch job.

Returns:
- results: The translated sentences.
"""


def retrieve_batch_results(batch_id):

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
            results.append(
                result["response"]["body"]["choices"][0]["message"]["content"]
            )

        return results
    except RequestException as e:
        print(f"Error retrieving batch results: {e}")
        return []

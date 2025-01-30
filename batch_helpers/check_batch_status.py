import os
from dotenv import load_dotenv
from openai import OpenAI
from requests.exceptions import RequestException

load_dotenv()
client = OpenAI(api_key=os.getenv("OpenAI_API_KEY"))


"""
Check the status of a batch job.

Parameters:
- batch_id: The ID of the batch job to check.

Returns:
- batch_status: The status of the batch job.
"""


def check_batch_status(batch_id):

    try:
        batch = client.batches.retrieve(batch_id)
        return batch["status"]
    except RequestException as e:
        print(f"Error checking batch status: {e}")
        return "failed"

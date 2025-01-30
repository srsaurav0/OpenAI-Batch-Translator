import os
from dotenv import load_dotenv
from openai import OpenAI
from requests.exceptions import RequestException


load_dotenv()
client = OpenAI(api_key=os.getenv("OpenAI_API_KEY"))


"""
Cancel a batch job.

Parameters:
- batch_id: The ID of the batch job to cancel.

Returns:
- batch: The updated batch object after cancellation.
"""


def cancel_batch(batch_id):

    try:
        batch = client.batches.cancel(batch_id)
        return batch
    except RequestException as e:
        print(f"Error cancelling batch: {e}")
        return None

from openai import OpenAI
from requests.exceptions import RequestException
import yaml


def load_config(file_path="config.yml"):
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
    return config


# Load the configuration
config = load_config()

client = OpenAI(api_key=config.get("openai_api_key"))


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

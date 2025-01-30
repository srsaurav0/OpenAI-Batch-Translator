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

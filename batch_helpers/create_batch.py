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
Create a batch job using the uploaded file.

Parameters:
- file_id: The ID of the uploaded file.
- completion_window: The time window for batch completion.

Returns:
- batch_id: The ID of the created batch job.
"""


def create_batch(file_id, completion_window="24h"):

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

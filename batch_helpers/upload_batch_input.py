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
Upload the batch input file to OpenAI's servers.

Parameters:
- filename: The name of the batch input file to upload.

Returns:
- file_id: The ID of the uploaded file, used for creating the batch.
"""


def upload_batch_input(filename):

    try:
        with open(filename, "rb") as f:
            file = client.files.create(file=f, purpose="batch")
        return file.id
    except RequestException as e:
        print(f"Error uploading file: {e}")
        return None

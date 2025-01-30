import os
from dotenv import load_dotenv
from openai import OpenAI
from requests.exceptions import RequestException

load_dotenv()
client = OpenAI(api_key=os.getenv("OpenAI_API_KEY"))


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

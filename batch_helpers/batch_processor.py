from datetime import datetime, timezone
import json
import os
from openai import OpenAI
from requests.exceptions import RequestException
import yaml

class BatchProcessor:
    def __init__(self, config_path="config.yml"):
        self.config = self.load_config(config_path)
        self.client = OpenAI(api_key=self.config.get("openai_api_key"))
    
    def load_config(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def create_batch(self, file_id, completion_window="24h"):
        try:
            batch = self.client.batches.create(
                input_file_id=file_id,
                endpoint="/v1/chat/completions",
                completion_window=completion_window,
            )
            return batch.id
        except RequestException as e:
            print(f"Error creating batch: {e}")
            return None

    def extract_content_from_file(self, file_path, batch_id):
        output_dir = f"results/list/{batch_id}"
        os.makedirs(output_dir, exist_ok=True)
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    data = json.loads(line)
                    content = (
                        data.get("response", {})
                        .get("body", {})
                        .get("choices", [{}])[0]
                        .get("message", {})
                        .get("content")
                    )
                    custom_id = data.get("custom_id")
                    if content:
                        content = content.replace("\\n", "\n")  # Ensure proper new lines
                        output_filename = os.path.join(output_dir, f"{custom_id}.txt")
                        with open(output_filename, "w", encoding="utf-8") as file:
                            file.write(content)
                        print(f"Extracted content saved to {output_filename}")
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")

    def prepare_batch_input(self, source_lang, target_lang, texts, filename="inputs/batchinput.jsonl"):
        filename = f"inputs/{next(iter(texts))}.jsonl"
        with open(filename, "w", encoding="utf-8") as f:
            for key, value in texts.items():
                request = {
                    "custom_id": f"rentbyowner.com-{key}",
                    "method": "POST",
                    "url": "/v1/chat/completions",
                    "body": {
                        "model": "gpt-4o-mini",
                        "messages": [
                            {
                                "role": "system",
                                "content": f"Translate the sentence from {source_lang} to {target_lang}. \n"
                                "Keep all HTML tags, attributes, and links intact. \n"
                                "Keep all templates intact. \n"
                                "Translate only the visible text between the tags. \n"
                                "Preserve the exact text of 'Rent By Owner™' and 'Rent by Owner' without translation or modification.\n"
                                "Preserve original spacing and line breaks without adding or removing any. \n"
                                "Ensure that the original formatting, including indentation and line breaks, is preserved in the output."
                            },
                            {"role": "user", "content": value},
                        ],
                        "max_tokens": 5000,
                    },
                }
                f.write(json.dumps(request) + "\n")
        return filename

    def retrieve_batch_results(self, batch_id, output_file="batch_output.jsonl"):
        try:
            batch = self.client.batches.retrieve(batch_id)
            if batch.status != "completed":
                print(f"Batch {batch_id} is {batch.status}. Wait until completed.")
                return [], {}

            output_id = batch.output_file_id
            file_response = self.client.files.content(output_id)
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(file_response.text)

            results = []
            with open(output_file, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        data = json.loads(line)
                        custom_id = data.get("custom_id")
                        response = data.get("response", {})
                        error = data.get("error")
                        if error is not None or response.get("status_code") != 200:
                            print(f"Skipping invalid entry (custom_id: {custom_id}): {error}")
                            continue

                        body = response.get("body", {})
                        choices = body.get("choices", [{}])
                        message = choices[0].get("message", {}) if choices else {}
                        content = message.get("content", "")
                        usage = body.get("usage", {})
                        results.append(
                            {
                                "custom_id": custom_id,
                                "content": content,
                                "prompt_tokens": usage.get("prompt_tokens", 0),
                                "completion_tokens": usage.get("completion_tokens", 0),
                                "total_tokens": usage.get("total_tokens", 0),
                            }
                        )
                    except json.JSONDecodeError:
                        print(f"Failed to parse line: {line}")
            return results
        except RequestException as e:
            print(f"Request failed: {e}")
            return []

    def upload_batch_input(self, filename):
        try:
            with open(filename, "rb") as f:
                file = self.client.files.create(file=f, purpose="batch")
                return file.id
        except RequestException as e:
            print(f"Error uploading file: {e}")
            return None
        
    
    def get_batch_duration(self, batch_id):
        batch_info = self.client.batches.retrieve(batch_id)
        
        # Extract timestamps
        created_at = datetime.fromtimestamp(batch_info['created_at'], timezone.utc)
        in_progress_at = datetime.fromtimestamp(batch_info['in_progress_at'], timezone.utc) if batch_info['in_progress_at'] else None
        completed_at = datetime.fromtimestamp(batch_info['completed_at'], timezone.utc) if batch_info['completed_at'] else None
        failed_at = datetime.fromtimestamp(batch_info['failed_at'], timezone.utc) if batch_info['failed_at'] else None
        expired_at = datetime.fromtimestamp(batch_info['expired_at'], timezone.utc) if batch_info['expired_at'] else None

        # Calculate duration based on the current status
        current_time = datetime.now(timezone.utc)
        
        if batch_info['status'] == "in_progress" and in_progress_at:
            duration = current_time - in_progress_at
            return f"Batch has been in progress for {duration}."
        
        elif batch_info['status'] == "completed" and completed_at:
            duration = completed_at - (in_progress_at if in_progress_at else created_at)
            return f"Batch completed in {duration}."
        
        elif batch_info['status'] == "failed" and failed_at:
            duration = failed_at - (in_progress_at if in_progress_at else created_at)
            return f"Batch failed after {duration}."
        
        elif batch_info['status'] == "expired" and expired_at:
            duration = expired_at - (in_progress_at if in_progress_at else created_at)
            return f"Batch expired after {duration}."
        
        else:
            return f"Batch status: {batch_info['status']}. Unable to determine duration."

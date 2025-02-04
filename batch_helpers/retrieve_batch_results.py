import json
from openai import OpenAI
from requests.exceptions import RequestException
import yaml


def load_config(file_path="config.yml"):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


config = load_config()
client = OpenAI(api_key=config.get("openai_api_key"))


def retrieve_batch_results(batch_id, output_file="batch_output.jsonl"):
    """Retrieve and process batch results with custom_id mapping."""
    try:
        batch = client.batches.retrieve(batch_id)
        if batch.status != "completed":
            print(f"Batch {batch_id} is {batch.status}. Wait until completed.")
            return [], {}

        # Save raw output file
        output_id = batch.output_file_id
        file_response = client.files.content(output_id)
        with open(output_file, "w") as f:
            f.write(file_response.text)

        # Process results
        results = []
        total_usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        
        with open(output_file, "r") as f:
            for line in f:
                try:
                    data = json.loads(line)
                    custom_id = data.get("custom_id")
                    response = data.get("response", {})
                    error = data.get("error")

                    # Skip errored entries (shouldn't be in output file normally)
                    if error is not None or response.get("status_code") != 200:
                        print(f"Skipping invalid entry (custom_id: {custom_id}): {error}")
                        continue

                    # Extract content
                    body = response.get("body", {})
                    choices = body.get("choices", [{}])
                    message = choices[0].get("message", {}) if choices else {}
                    content = message.get("content", "")

                    # Extract usage and accumulate totals
                    usage = body.get("usage", {})
                    results.append({
                        "custom_id": custom_id,
                        "content": content,
                        "prompt_tokens": usage.get("prompt_tokens", 0),
                        "completion_tokens": usage.get("completion_tokens", 0),
                        "total_tokens": usage.get("total_tokens", 0)
                    })

                    total_usage["prompt_tokens"] += usage.get("prompt_tokens", 0)
                    total_usage["completion_tokens"] += usage.get("completion_tokens", 0)
                    total_usage["total_tokens"] += usage.get("total_tokens", 0)

                except json.JSONDecodeError:
                    print(f"Failed to parse line: {line}")
        
        return results, total_usage

    except RequestException as e:
        print(f"Request failed: {e}")
        return []
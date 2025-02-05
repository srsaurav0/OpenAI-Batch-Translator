import json
import os


def extract_content_from_file(file_path, batch_id):
    """
    Reads a text file containing JSON-like entries and extracts the 'content' field as raw text.

    :param file_path: Path to the text file containing JSON-like entries.
    :param batch_id: Batch ID for organizing output files.
    :return: List of extracted 'content' field values.
    """
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
                        file.write(content)  # Save as plain text

                    print(f"Extracted content saved to {output_filename}")
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

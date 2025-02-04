import json


"""
Prepare a .jsonl file with translation requests.

Parameters:
- source_lang: Source language code (e.g., 'en' for English).
- target_lang: Target language code (e.g., 'fr' for French).
- texts: List of texts to be translated.
- filename: Output filename for the .jsonl file.

Returns:
- The filename of the generated batch input file.
"""


def prepare_batch_input(source_lang, target_lang, texts, filename="batchinput.jsonl"):

    with open(filename, "w", encoding="utf-8") as f:
        for idx, text in enumerate(texts):
            request = {
                "custom_id": f"request-{idx}",
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
                            'Do not change the string "Rent By Owner™" or "Rent by Owner". \n'
                            "Do not include any extra new line characters ('\\n') or whitespace. \n"
                            "Ensure that the original formatting, including indentation and line breaks, is preserved in the output."
                        },
                        {"role": "user", "content": text},
                    ],
                    "max_tokens": 5000,  # Adjust based on expected sentence length
                },
            }
            f.write(json.dumps(request) + "\n")

    return filename

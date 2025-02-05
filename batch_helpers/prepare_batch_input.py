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


def prepare_batch_input(source_lang, target_lang, texts, filename="inputs/batchinput.jsonl"):
    filename = f"inputs/{next(iter(texts))}.jsonl"
    with open(filename, "w", encoding="utf-8") as f:
        for key, value in texts.items():
            request = {
                "custom_id": f"rentbyowner.com-{key}",
                # rentbyowner.com-{key}
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
                    "max_tokens": 5000,  # Adjust based on expected sentence length
                },
            }
            f.write(json.dumps(request) + "\n")

    return filename

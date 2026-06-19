import json
import re


def extract_split_json(text: str) -> dict:
    """Extract the expected split JSON payload from a model response."""
    clean_text = text.strip()

    try:
        return json.loads(clean_text)
    except json.JSONDecodeError:
        json_match = re.search(r"(\{.*?\})", clean_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))

    raise ValueError("The response could not be parsed into valid Split JSON framework.")

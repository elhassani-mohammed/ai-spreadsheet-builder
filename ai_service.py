import pandas as pd
from openai import OpenAI

from config import OPENROUTER_BASE_URL, SYSTEM_INSTRUCTION
from json_utils import extract_split_json


def generate_dataframe(api_key: str, model_name: str, user_prompt: str) -> pd.DataFrame:
    """Generate a dataframe from the user's prompt through OpenRouter."""
    client = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=api_key)

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": SYSTEM_INSTRUCTION},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.1,
    )

    raw_payload = response.choices[0].message.content
    parsed_json = extract_split_json(raw_payload)
    return pd.DataFrame(data=parsed_json["data"], columns=parsed_json["columns"])

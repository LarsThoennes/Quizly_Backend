import json
import re

def parse_gemini_json(response_text: str) -> dict:
    """
    Parses and cleans a JSON response returned by the Gemini AI model.

    - Removes Markdown code block formatting if present
    - Validates that the response is not empty
    - Converts the cleaned string into a Python dictionary
    - Raises a ValueError if the response is empty or invalid
    """
    if not response_text or response_text.strip() == "":
        raise ValueError("Gemini returned empty response")

    cleaned = response_text.strip()

    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```json", "", cleaned)
        cleaned = re.sub(r"^```", "", cleaned)
        cleaned = re.sub(r"```$", "", cleaned)

    cleaned = cleaned.strip()

    return json.loads(cleaned)

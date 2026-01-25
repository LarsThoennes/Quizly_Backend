import json
import re

def parse_gemini_json(response_text: str) -> dict:
    if not response_text or response_text.strip() == "":
        raise ValueError("Gemini returned empty response")

    cleaned = response_text.strip()

    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```json", "", cleaned)
        cleaned = re.sub(r"^```", "", cleaned)
        cleaned = re.sub(r"```$", "", cleaned)

    cleaned = cleaned.strip()

    return json.loads(cleaned)

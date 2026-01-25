from google import genai
import os

def generate_gemini_response(prompt: str) -> str:
    """
    Generates an AI response using the Gemini language model.

    - Sends a prompt to the Gemini API
    - Uses the configured API key from environment variables
    - Returns the generated text response
    """
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
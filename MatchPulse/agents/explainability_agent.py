import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-flash-latest")


def explain_moment():

    prompt = """
You are a football analyst.

Explain why possession, passing accuracy
and pressure contribute to scoring chances.

Rules:
- Maximum 50 words
- Plain text only
- No HTML
- No markdown
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:
        return (
            "Sustained possession and accurate passing "
            "create space, increase pressure and improve "
            "the likelihood of scoring."
        )
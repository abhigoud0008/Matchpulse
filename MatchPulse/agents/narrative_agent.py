import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-flash-latest")


def generate_narrative(stats):

    prompt = f"""
You are a professional football analyst.

ONLY use the statistics given below.

Possession: {stats['possession']}%
Pass Accuracy: {stats['pass_accuracy']}%
Goals: {stats['goals']}
Shots: {stats['shots']}
Pressure Index: {stats['pressure_index']}

Rules:
- Do NOT invent scores
- Do NOT invent players
- Do NOT invent goals
- Do NOT invent minutes
- Use only provided statistics
- Plain text only
- Maximum 50 words

Generate:
1. Match Narrative
2. Key Insight
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:
        return (
            f"Blue FC controlled the match with "
            f"{stats['possession']}% possession and "
            f"{stats['pass_accuracy']}% pass accuracy."
        )

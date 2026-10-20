import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-flash-latest")


def generate_recap(stats):

    prompt = f"""
Create a football match recap.

Statistics:

Possession = {stats['possession']}%
Goals = {stats['goals']}
Shots = {stats['shots']}
Pressure Index = {stats['pressure_index']}

Rules:
- Use only these statistics
- Do NOT invent players
- Do NOT invent teams
- Do NOT invent scores
- Maximum 80 words
- Plain text only

Include:
1. Match Summary
2. Key Takeaway
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:
        return (
            "The match was controlled through strong possession "
            "and sustained attacking pressure."
        )
import json
from openai import OpenAI

client = OpenAI()


def analyze_resume(text: str) -> dict:
    """
    Analyze a resume with an LLM and return structured insights as a dict.
    """
    prompt = f"""
You are an expert resume evaluator and hiring strategist.

Analyze the following resume text and return structured insights.

Resume:
{text}

Return a VALID JSON object with the following keys:
- "strengths": list of strings
- "weaknesses": list of strings
- "recommended_skills": list of strings
- "ats_score": integer from 0 to 100
- "rewritten_summary": string

IMPORTANT:
- Return ONLY a JSON object.
- Do NOT include markdown.
- Do NOT include backticks.
- Do NOT include any explanation.
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
    )

    content = response.choices[0].message.content.strip()

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        # Fallback in case the model does something unexpected
        data = {"raw_response": content}

    return data


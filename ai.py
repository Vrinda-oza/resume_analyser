from click import prompt
from openai import OpenAI
import json
from dotenv import load_dotenv
import os

from pyexpat.errors import messages

load_dotenv()

client = OpenAI(
    #api_key=os.getenv("OPENAI_API_KEY")
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def analyze_resume(resume_text,user_goal):
    prompt=f"""
You are a senior software engineer and an expert hiring manager.

Evaluate the resume based on the user's career goal.
User goal: "{user_goal}"

STRICT RULES:
- Extract and list all relevant skills for this goal in detail.
- REMOVE completely irrelevant tools [e.g., excel for backend, etc.].
- Identify real technical gaps and explain them.
- Provide a highly detailed, step-by-step roadmap specifically to bridge those missing fields.
- Provide a robust list of realistic interview questions tailored to this target role.
- Make the output highly specific and comprehensive based on the goal.

Return ONLY a valid JSON object matching this structure:
{{
"skills": ["Detailed skill 1", "Detailed skill 2"],
"missing_skills": ["Detailed missing skill 1", "Detailed missing skill 2"],
"roadmap": ["Step 1: Deep explanation of what to learn", "Step 2: Practical project to build"],
"interview_questions": ["Question 1 (with brief context)", "Question 2"]
}}
Resume:
{resume_text}
"""
    try:
        response=client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            messages=[
                {"role": "system","content":"You'rea strict hiring manager."},
                {"role":"user","content":prompt}
            ]
        )
        content=response.choices[0].message.content.strip()

        start=content.find("{")
        end=content.rfind("}")+1
        return json.loads(content[start:end])
    except Exception as e:
        return{
            "skills":[],
            "missing_skills":[],
            "roadmap":[],
            "interview_questions":[],
            "error":str(e)
        }

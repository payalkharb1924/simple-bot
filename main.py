from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()

# PASTE YOUR GEMINI API KEY HERE
genai.configure(api_key="AIzaSyD-m66DkbQfGqIVFLA3Ud5uKifiTJ75Kfc")


class InterviewRequest(BaseModel):
    role: str
    experience: str


@app.post("/interview")
async def interview_bot(data: InterviewRequest):

    prompt = f"""
    You are a professional interviewer.
    Ask one interview question at a time.

    Role: {data.role}
    Experience Level: {data.experience}

    Question should be clear and professional.
    """

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    question = response.text

    return {"question": question}

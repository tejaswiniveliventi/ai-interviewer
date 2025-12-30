from pydantic import BaseModel
from typing import Optional


class InterviewStartRequest(BaseModel):
    role: str
    experience: str


class InterviewStartResponse(BaseModel):
    session_id: str
    question: str

class InterviewAnswerRequest(BaseModel):
    session_id: str
    answer: str


class InterviewAnswerResponse(BaseModel):
    feedback: str
    next_question: str

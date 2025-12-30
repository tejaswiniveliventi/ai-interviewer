from pydantic import BaseModel
from typing import Optional


class InterviewStartRequest(BaseModel):
    role: str
    experience: str


class InterviewStartResponse(BaseModel):
    session_id: str
    question: str

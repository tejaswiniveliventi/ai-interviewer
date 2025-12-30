from fastapi import FastAPI
from app.models import InterviewStartRequest, InterviewStartResponse
from app.state import create_session
from app.interview import generate_first_question

app = FastAPI(
    title="AI Interviewer",
    description="An AI-powered interview platform to help candidates prepare for job interviews.",
    version="0.1.0"
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI Interviewer API!"}
def health_check():
    return {"status": "backend is running smoothly"}

@app.post("/interview/start", response_model=InterviewStartResponse)
def start_interview(request: InterviewStartRequest):
    session = create_session(request.role, request.experience)
    question = get_first_question(request.role, request.experience)

    return {
        "session_id": session["session_id"],
        "question": question
    }
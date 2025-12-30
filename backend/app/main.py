from fastapi import FastAPI
from app.models import InterviewStartRequest, InterviewStartResponse,InterviewAnswerRequest, InterviewAnswerResponse
from app.state import create_session,get_session
from app.interview import generate_first_question,evaluate_answer

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
@app.post("/interview/answer", response_model=InterviewAnswerResponse)
def answer_interview(request: InterviewAnswerRequest):
    session = get_session(request.session_id)

    if not session:
        return {"feedback": "Invalid session", "next_question": ""}

    evaluation = evaluate_answer(session, request.answer)

    # Update session
    session["questions_asked"] += 1
    session["difficulty"] = (
        "hard" if evaluation["difficulty"] == "increase"
        else "easy" if evaluation["difficulty"] == "decrease"
        else session["difficulty"]
    )

    session["history"].append({
        "answer": request.answer,
        "feedback": evaluation["feedback"]
    })

    return {
        "feedback": evaluation["feedback"],
        "next_question": evaluation["next_question"]
    }

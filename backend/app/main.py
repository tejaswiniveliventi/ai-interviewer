from fastapi import FastAPI

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

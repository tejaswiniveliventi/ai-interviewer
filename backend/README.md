# AI Salesforce Interviewer – Backend

Backend service for an adaptive AI-powered Salesforce interview simulator.

## Tech Stack
- Python
- FastAPI
- LLM (Groq / OpenAI)
- In-memory session state

## Running Locally

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

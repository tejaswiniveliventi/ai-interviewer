from datetime import datetime
from typing import Dict
import uuid

interview_sessions: Dict[str, dict] = {}


def create_session(role: str, experience: str) -> dict:
    session_id = str(uuid.uuid4())

    session = {
        "session_id": session_id,
        "role": role,
        "experience": experience,
        "start_time": datetime.utcnow(),
        "questions_asked": 0,
        "difficulty": "medium",
        "history": []
    }

    interview_sessions[session_id] = session
    return session

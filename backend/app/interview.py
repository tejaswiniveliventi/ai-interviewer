import json
from app.llm import call_llm
from app.prompts import (
    SYSTEM_INTERVIEW_PROMPT,
    FIRST_QUESTION_PROMPT,
    EVALUATE_ANSWER_PROMPT
)


def generate_first_question(role: str, experience: str) -> str:
    user_prompt = FIRST_QUESTION_PROMPT.format(
        role=role,
        experience=experience
    )

    return call_llm(SYSTEM_INTERVIEW_PROMPT, user_prompt).strip()


def evaluate_answer(session: dict, answer: str) -> dict:
    user_prompt = EVALUATE_ANSWER_PROMPT.format(
        answer=answer,
        role=session["role"],
        experience=session["experience"],
        difficulty=session["difficulty"],
        questions_asked=session["questions_asked"]
    )

    response = call_llm(SYSTEM_INTERVIEW_PROMPT, user_prompt)

    return json.loads(response)

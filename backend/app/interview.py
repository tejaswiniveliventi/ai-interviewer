from app.llm import call_llm
from app.prompts import SYSTEM_INTERVIEW_PROMPT, FIRST_QUESTION_PROMPT


def generate_first_question(role: str, experience: str) -> str:
    user_prompt = FIRST_QUESTION_PROMPT.format(
        role=role,
        experience=experience
    )

    question = call_llm(
        system_prompt=SYSTEM_INTERVIEW_PROMPT,
        user_prompt=user_prompt
    )

    return question.strip()

from pydantic import BaseModel
from typing import List, Dict

class QuizSubmission(BaseModel):
    student_id: str
    quiz_id: str
    responses: Dict[str, str]  # {"Q1": "A", "Q2": "B"}

class QuizResult(BaseModel):
    student_id: str
    quiz_id: str
    correct: int
    incorrect: int
    score: float
    feedback: str
    chart_data: Dict[str, int]

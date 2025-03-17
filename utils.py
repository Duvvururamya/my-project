import numpy as np
from models import QuizSubmission, QuizResult

# Define correct answers
CORRECT_ANSWERS = {"Q1": "A", "Q2": "C", "Q3": "B", "Q4": "D", "Q5": "A"}

def evaluate_quiz(submission: QuizSubmission) -> QuizResult:
    correct = sum(1 for q, ans in submission.responses.items() if CORRECT_ANSWERS.get(q) == ans)
    incorrect = len(submission.responses) - correct
    score = (correct / len(CORRECT_ANSWERS)) * 100

    feedback = generate_feedback(score)
    chart_data = {"Correct": correct, "Incorrect": incorrect}

    return QuizResult(
        student_id=submission.student_id,
        quiz_id=submission.quiz_id,
        correct=correct,
        incorrect=incorrect,
        score=score,
        feedback=feedback,
        chart_data=chart_data
    )

def generate_feedback(score: float) -> str:
    if score >= 90:
        return "Excellent performance! Keep it up!"
    elif 60 <= score < 90:
        return "Good job! Revise the missed topics."
    else:
        return "Needs improvement. Consider reviewing key concepts."

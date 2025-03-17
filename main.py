from fastapi import FastAPI, WebSocket
from models import QuizSubmission, QuizResult
from utils import evaluate_quiz
import json

app = FastAPI()

@app.websocket("/ws/quiz")
async def quiz_websocket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            quiz_data = json.loads(data)

            # Validate & Evaluate Quiz
            result = evaluate_quiz(QuizSubmission(**quiz_data))

            # Send back results
            await websocket.send_text(json.dumps(result.dict()))

    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()


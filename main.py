from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from data import fetch_questions
from question_model import Question
from quiz_brain import QuizBrain

app = FastAPI()
templates = Jinja2Templates(directory="templates")

question_data = fetch_questions(10)
question_bank = [Question(q["text"], q["answer"]) for q in question_data]
quiz = QuizBrain(question_bank)

@app.get("/", response_class=HTMLResponse)
async def quiz_page(request: Request):
    if not quiz.still_has_questions():
        final_score = quiz.score
        feedback = quiz.feedback_text(final_score)
        return templates.TemplateResponse("quiz.html", {
            "request": request,
            "question": None,
            "score": final_score,
            "feedback": feedback
        })

    current_q = quiz.get_current_question()
    return templates.TemplateResponse("quiz.html", {
        "request": request,
        "question": current_q.text,
        "score": quiz.score,
        "feedback": None
    })

@app.post("/answer", response_class=HTMLResponse)
async def answer(request: Request, answer: str = Form(...)):
    quiz.check_answer(answer)
    return await quiz_page(request)

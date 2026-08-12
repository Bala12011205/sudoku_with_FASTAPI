from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sudoku import generate_puzzle

app = FastAPI(title="Sudoku Game")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/new-game")
def new_game(difficulty: str = "easy"):
    # Define hole count based on selected difficulty
    holes = 30 if difficulty == "easy" else 42 if difficulty == "medium" else 54
    puzzle, solution = generate_puzzle(holes)
    return {"puzzle": puzzle, "solution": solution}
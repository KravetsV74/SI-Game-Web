from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Своя Игра</h1>
    <p>Сервер работает!</p>
    """
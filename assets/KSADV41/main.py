from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def serve_home():
    with open("KSADV41.html", "r", encoding="utf-8") as file:
        return file.read()

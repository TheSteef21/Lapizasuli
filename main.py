from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/TSADV41", response_class=HTMLResponse)
async def get_tsadv41():
    # Asegúrate de tener el archivo guardado en tu directorio
    with open("templates/TSADV41.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

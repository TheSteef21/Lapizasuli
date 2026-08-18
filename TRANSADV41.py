from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import os

app = FastAPI(title="SADV41 Sovereign Hub", version="1.0.0")

@app.get("/", response_class=HTMLResponse)
async def logia_maestra():
    # El origen es 0. Servimos la interfaz transfigurada desde la nueva ruta.
    # Se actualizó la ruta para que coincida con tu repositorio en GitHub
    ruta_html = os.path.join("assets", "TRANSFIGURACION", "logia_unificada.html")
    
    with open(ruta_html, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    # Ejecutar servidor en el puerto 8000
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

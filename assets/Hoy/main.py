from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

ARCHIVO_JSON = "noticias.json"

def cargar_noticias():
    if os.path.exists(ARCHIVO_JSON):
        try:
            with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

# Ruta principal: Previsualización de tarjetas estilo notificación
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    noticias_actualizadas = cargar_noticias()
    return templates.TemplateResponse("index.html", {"request": request, "noticias": noticias_actualizadas})

# Ruta para ver el panel de administración web (admin.html)
@app.get("/admin", response_class=HTMLResponse)
async def admin_panel(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

# Ruta API para procesar la inyección dinámica de noticias al Nodo
@app.post("/api/actualizar")
async def agregar_noticia_dinamica(
    source: str = Form(...), 
    title: str = Form(...), 
    image: str = Form(...), 
    time: str = Form(...)
):
    noticias = cargar_noticias()
                
    nueva_noticia = {
        "source": source,
        "time": time,
        "title": title,
        "image": image,
        "url": "#"
    }
    
    # Insertar la nueva noticia al inicio de la lista (Ley de Restitución en vivo)
    noticias.insert(0, nueva_noticia)
    
    # Guardar los cambios en el archivo JSON del servidor
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=4)
        
    return {
        "status": "¡Noticia inyectada con éxito al Nodo SADV41!", 
        "total_noticias": len(noticias)
    }

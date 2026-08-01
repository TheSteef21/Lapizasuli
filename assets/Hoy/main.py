from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import os
import requests
from bs4 import BeautifulSoup

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

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    noticias_actualizadas = cargar_noticias()
    return templates.TemplateResponse("index.html", {"request": request, "noticias": noticias_actualizadas})

@app.get("/admin", response_class=HTMLResponse)
async def admin_panel(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

# Endpoint inteligente para procesar enlaces o inserción directa
@app.post("/api/actualizar")
async def agregar_noticia_dinamica(
    source: str = Form("Google Noticias"), 
    title: str = Form(None), 
    image: str = Form(None), 
    time: str = Form("Ahora"),
    url: str = Form(None)
):
    noticias = cargar_noticias()
    
    # Si pegas un enlace oficial de Google o web, intentamos extraer los metadatos automáticamente
    titulo_final = title
    imagen_final = image
    
    if url and url.startswith("http"):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            resp = requests.get(url, headers=headers, timeout=6)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                
                # Extraer título real si no se proveyó uno manual
                if not titulo_final:
                    t_tag = soup.find('title')
                    titulo_final = t_tag.text.strip() if t_tag else "Noticia oficial del Nodo"
                
                # Extraer imagen OpenGraph si no se proveyó una manual
                if not imagen_final or imagen_final == "":
                    img_tag = soup.find('meta', property='og:image')
                    imagen_final = img_tag['content'] if img_tag else "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?q=80&w=600&auto=format&fit=crop"
            else:
                titulo_final = titulo_final or "Enlace registrado en el Nodo"
                imagen_final = imagen_final or "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?q=80&w=600&auto=format&fit=crop"
        except Exception:
            titulo_final = titulo_final or "Enlace oficial SADV41"
            imagen_final = imagen_final or "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?q=80&w=600&auto=format&fit=crop"
    
    nueva_noticia = {
        "source": source,
        "time": time,
        "title": titulo_final or "Sin título",
        "image": imagen_final or "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?q=80&w=600&auto=format&fit=crop",
        "url": url if url else "#"
    }
    
    noticias.insert(0, nueva_noticia)
    
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=4)
        
    return {
        "status": "¡Noticia oficial inyectada con éxito al Nodo SADV41!", 
        "total_noticias": len(noticias)
    }

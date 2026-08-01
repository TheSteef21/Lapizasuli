from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Datos de ejemplo basados en tus notificaciones recientes
NOTICIAS_EJEMPLO = [
    {
        "source": "Montevideo Portal",
        "time": "8:38 p.m.",
        "title": "“Significativo y violento”: las impactantes imágenes de un tornado que golpeó a Argentina",
        "image": "https://images.unsplash.com/photo-1527482797697-8795b05813fe?q=80&w=600&auto=format&fit=crop",
        "url": "#"
    },
    {
        "source": "BioBioChile",
        "time": "4:08 p.m.",
        "title": "¿Puede España ser excluido del Espacio Schengen debido a la crisis migratoria en Ceuta?",
        "image": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?q=80&w=600&auto=format&fit=crop",
        "url": "#"
    },
    {
        "source": "ESPN Deportes",
        "time": "31/7/2026",
        "title": "Cuándo juegan Real Madrid vs Fiorentina: equipo, fecha, hora y TV en vivo",
        "image": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=600&auto=format&fit=crop",
        "url": "#"
    },
    {
        "source": "La Estrella de Panamá",
        "time": "3:14 p.m.",
        "title": "China reafirma apoyo a la soberanía del Canal de Panamá",
        "image": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?q=80&w=600&auto=format&fit=crop",
        "url": "#"
    }
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "noticias": NOTICIAS_EJEMPLO})

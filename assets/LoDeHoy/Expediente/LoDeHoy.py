from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, List
import shutil
import os
import json
from datetime import datetime

app = FastAPI(title="SADV41 Expedientes Engine", version="2.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Estructura de carpetas solicitada: assets/LoDeHoy/Expedientes
BASE_EXPEDIENTES_DIR = "assets/LoDeHoy/Expedientes"
os.makedirs(BASE_EXPEDIENTES_DIR, exist_ok=True)

# Servir archivos estáticos para previsualización multimedia en el frontend
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

class DailyRecord(BaseModel):
    id: str
    timestamp: str
    target: str  # "GSADV41", "Logia" o "Ambos"
    content: str
    source_url: Optional[str] = None
    media_path: Optional[str] = None

# Archivo maestro acumulativo general o por expediente diario
MASTER_FEED_FILE = os.path.join(BASE_EXPEDIENTES_DIR, "master_feed.json")

def load_db() -> List[dict]:
    if os.path.exists(MASTER_FEED_FILE):
        with open(MASTER_FEED_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_db(data: List[dict]):
    with open(MASTER_FEED_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@app.post("/api/submit-note")
async def submit_note(
    content: str = Form(...),
    source_url: Optional[str] = Form(None),
    target: str = Form("GSADV41"),
    file: Optional[UploadFile] = File(None)
):
    today_str = datetime.now().strftime("%Y-%m-%d")
    # Subcarpeta diaria dentro de Expedientes para llevar secuencia
    day_folder = os.path.join(BASE_EXPEDIENTES_DIR, today_str)
    os.makedirs(day_folder, exist_ok=True)
    
    media_path = None
    if file and file.filename:
        file_location = os.path.join(day_folder, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        # Ruta accesible por el servidor estático
        media_path = f"/assets/LoDeHoy/Expedientes/{today_str}/{file.filename}"

    record_id = f"note-{int(datetime.now().timestamp())}"
    new_entry = {
        "id": record_id,
        "date_folder": today_str,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "target": target,
        "content": content,
        "source_url": source_url,
        "media_path": media_path
    }

    db = load_db()
    db.insert(0, new_entry) # Nuevas entradas al inicio
    save_db(db)

    # Opcional: Guardar también un JSON específico del día en su subcarpeta para respaldo de expediente limpio
    day_json_path = os.path.join(day_folder, "expediente_dia.json")
    day_items = [item for item in db if item["date_folder"] == today_str]
    with open(day_json_path, "w", encoding="utf-8") as f:
        json.dump(day_items, f, indent=4, ensure_ascii=False)

    return {"status": "success", "message": f"Expediente de {today_str} actualizado correctamente", "data": new_entry}

@app.get("/api/feed")
def get_feed(target: Optional[str] = None):
    db = load_db()
    if target and target != "Todos":
        filtered = [item for item in db if item["target"] == target or item["target"] == "Ambos"]
        return filtered
    return db

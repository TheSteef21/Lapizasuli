from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, List
import shutil
import os
import json
from datetime import datetime

app = FastAPI(title="SADV41 Expedientes Engine", version="2.3.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directorio base apuntando a la misma ruta actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Montar estáticos desde esta misma carpeta
app.mount("/expedientes_assets", StaticFiles(directory=BASE_DIR), name="expedientes_assets")

MASTER_FEED_FILE = os.path.join(BASE_DIR, "master_feed.json")

# Clave secreta obtenida desde las variables de entorno de Render (`CLAVE_SECRETA_LOGIA`)
CLAVE_LOGIA_SERVER = os.getenv("CLAVE_SECRETA_LOGIA", "SADV41-DEFAULT-KEY")

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
    day_folder = os.path.join(BASE_DIR, today_str)
    os.makedirs(day_folder, exist_ok=True)
    
    media_path = None
    if file and file.filename:
        file_location = os.path.join(day_folder, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        media_path = f"/expedientes_assets/{today_str}/{file.filename}"

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
    db.insert(0, new_entry)
    save_db(db)

    return {"status": "success", "message": f"Expediente de {today_str} actualizado", "data": new_entry}

@app.get("/api/feed")
def get_feed(target: Optional[str] = None):
    db = load_db()
    if target and target != "Todos":
        filtered = [item for item in db if item["target"] == target or item["target"] == "Ambos"]
        return filtered
    return db

@app.post("/api/delete-source")
async def delete_source(record_id: str = Form(...), key: str = Form(...)):
    if key != CLAVE_LOGIA_SERVER:
        raise HTTPException(status_code=403, detail="Clave incorrecta. Acceso denegado por la Logia.")
    
    db = load_db()
    updated = False
    for item in db:
        if item["id"] == record_id:
            item["source_url"] = None
            updated = True
            break
            
    if updated:
        save_db(db)
        return {"status": "success", "message": "Fuente eliminada correctamente del registro"}
    
    raise HTTPException(status_code=404, detail="Registro no encontrado")

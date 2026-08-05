from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import datetime
import json
import os

app = FastAPI(title="SADV41TT Live Sync Engine", version="2.0")

# Habilitar CORS para permitir la comunicación con el archivo HTML local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Transaccion(BaseModel):
    unidades: str
    medida: str
    marca: str
    monto: str
    metodo: str
    observaciones: Optional[str] = ""

class CierreJornada(BaseModel):
    fecha: str
    mision: str
    total_registros: int
    transacciones: List[Transaccion]

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

@app.post("/api/registrar")
async def guardar_registro_en_tiempo_real(datos: CierreJornada):
    try:
        nombre_archivo = os.path.join(DATA_DIR, f"registro_diario_{datos.fecha}.json")
        
        # Guardar / Sobrescribir el JSON actualizado del día
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(datos.dict(), f, ensure_ascii=False, indent=4)
            
        return {
            "status": "success", 
            "message": f"JSON actualizado correctamente para la fecha {datos.fecha}",
            "archivo": nombre_archivo
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

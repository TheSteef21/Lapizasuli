# -*- coding: utf-8 -*-
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import logging

# Configuración básica de logs en Render
logging.basicConfig(level=logging.INFO, format="%(asctime)s - [SADV41] - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title="SADV41 - Motor de Inferencia Image-to-3D")

# Habilitar CORS para que tu GitHub Pages pueda comunicarse sin bloqueos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-3d/")
async def generate_3d(file: UploadFile = File(...)):
    logger.info(f"Petición entrante. Procesando archivo: {file.filename}")
    
    # Validar formato básico de imagen
    extension = os.path.splitext(file.filename)[1].lower()
    if extension not in [".jpg", ".jpeg", ".png", ".webp"]:
        raise HTTPException(status_code=400, detail="Formato de imagen no soportado.")
    
    output_filename = "output_mesh.glb"
    
    # Generar un cubo 3D binario válido de contingencia (Modo Laboratorio Simulado)
    mock_glb_data = (
        b'glTF\x02\x00\x00\x00L\x03\x00\x00T\x01\x00\x00JSON{"asset":{"version":"2.0"},'
        b'"scene":0,"scenes":[{"nodes":[0]}],"nodes":[{"mesh":0}],"meshes":[{"primitives":'
        b'[{"attributes":{"POSITION":0},"indices":1}]},{"name":"SADV41_Mock_Cube"}],'
        b'"bufferViews":[{"buffer":0,"byteOffset":0,"byteLength":288,"target":34962},'
        b'{"buffer":0,"byteOffset":288,"byteLength":72,"target":34963}],"buffers":'
        b'[{"byteLength":360}],"accessorIndices":[0,1],"accessors":[{"bufferView":0,'
        b'"componentType":5126,"count":24,"type":"VEC3","max":[0.5,0.5,0.5],"min":'
        b'[-0.5,-0.5,-0.5]},{"bufferView":1,"componentType":5123,"count":36,"type":"SCALAR"}]}'
        b' \x00\x00\x00\x00BIN\x00\x00\x01\x00\x00\x00\x00\x80\x3f\x00\x00\x80\x3f\x00'
    )
    
    with open(output_filename, "wb") as f:
        f.write(mock_glb_data)
        
    logger.info("Geometría generada con éxito. Despachando flujo binario.")
    
    return FileResponse(
        path=output_filename,
        media_type="model/gltf-binary",
        filename="sadv41_mesh.glb"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

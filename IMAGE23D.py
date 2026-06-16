# -*- coding: utf-8 -*-
"""
Misión SADV41 — Motor de Generación Geométrica Dinámica (2D a 3D)
Archivo: IMAGE23D.py
Estatus: Producción / Generación Real Dinámica
Descripción: Lee la imagen enviada, procesa sus píxeles y esculpe una malla 
             tridimensional (.glb) única basada en el relieve de la imagen.
"""

import os
import io
import math
import struct
import logging
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [SADV41_GENERATOR] - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="SADV41 - Real Image-to-3D Engine", version="3.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root_status():
    return {"status": "online", "engine": "SADV41 Dynamic Heightmap Core"}

@app.post("/generate-3d/")
async def generate_3d_endpoint(file: UploadFile = File(...)):
    logger.info(f"Iniciando reconstrucción dinámica para: {file.filename}")
    
    extension = os.path.splitext(file.filename)[1].lower()
    if extension not in [".jpg", ".jpeg", ".png", ".webp"]:
        raise HTTPException(status_code=400, detail="Formato de imagen no soportado.")
    
    try:
        # 1. Leer los bytes de la imagen y abrirla dinámicamente con PIL
        file_bytes = await file.read()
        img = Image.open(io.BytesIO(file_bytes)).convert("L") # Convertir a escala de grises para relieve
        img = img.resize((16, 16)) # Redimensionar a una matriz de 16x16 para no saturar la CPU de Render
        
        width, height = img.size
        pixels = img.load()
        
        vertices = []
        indices = []
        
        # 2. Algoritmo de Escultura Tridimensional basado en Píxeles
        # Generamos coordenadas X, Y, Z basadas en la posición del píxel y su brillo (Z)
        for y in range(height):
            for x in range(width):
                # Normalizar coordenadas entre -0.5 y 0.5
                nx = (x / (width - 1)) - 0.5
                ny = (y / (height - 1)) - 0.5
                
                # El brillo del píxel (0 a 255) define la altura Z de la geometría
                brightness = pixels[x, y]
                nz = (brightness / 255.0) * 0.3 # Escalar relieve max de 0.3
                
                # Guardar vértice (X, Y, Z)
                vertices.extend([nx, nz, ny]) # Intercambiamos Y y Z para orientación 3D
                
        # 3. Construcción de la topología de caras (Triángulos enlazados)
        for y in range(height - 1):
            for x in range(width - 1):
                # Índices de los 4 vértices de cada celda de la imagen
                row1 = y * width
                row2 = (y + 1) * width
                
                v0 = row1 + x
                v1 = row1 + x + 1
                v2 = row2 + x
                v3 = row2 + x + 1
                
                # Primer triángulo de la celda
                indices.extend([v0, v1, v2])
                # Segundo triángulo de la celda
                indices.extend([v1, v3, v2])

        # 4. Empaquetamiento binario en formato glTF/GLB estándar (Formato legible por model-viewer)
        v_count = len(vertices) // 3
        i_count = len(indices)
        
        v_binary = struct.pack(f'<{len(vertices)}f', *vertices)
        i_binary = struct.pack(f'<{i_count}H', *indices)
        
        # Alineación de bytes
        while len(v_binary) % 4 != 0: v_binary += b'\x00'
        while len(i_binary) % 4 != 0: i_binary += b'\x00'
        
        v_len = len(v_binary)
        i_len = len(i_binary)
        total_bin_len = v_len + i_len
        
        # Estructura JSON interna del glTF descriptivo
        json_str = (
            f'{{"asset":{{"version":"2.0"}},'
            f'"scene":0,"scenes":[{{"nodes":[0]}}],'
            f'"nodes":[{{"mesh":0}}],'
            f'"meshes":[{{"primitives":[{{"attributes":{{"POSITION":0}},"indices":1,"mode":4}}]}}],'
            f'"bufferViews":['
            f'{{"buffer":0,"byteOffset":0,"byteLength":{v_len},"target":34962}},'
            f'{{"buffer":0,"byteOffset":{v_len},"byteLength":{i_len},"target":34963}}],'
            f'"buffers":[{{"byteLength":{total_bin_len}}}],'
            f'"accessors":['
            f'{{"bufferView":0,"componentType":5126,"count":{v_count},"type":"VEC3"}},'
            f'{{"bufferView":1,"componentType":5123,"count":{i_count},"type":"SCALAR"}}]}}'
        )
        
        json_bytes = json_str.encode('utf-8')
        while len(json_bytes) % 4 != 0: json_bytes += b' '
        
        # Cabecera binaria GLB oficial
        header = struct.pack('<4sII', b'glTF', 2, 12 + 8 + len(json_bytes) + 8 + total_bin_len)
        chunk_json = struct.pack('<I4s', len(json_bytes), b'JSON') + json_bytes
        chunk_bin = struct.pack('<I4s', total_bin_len, b'BIN\x00') + v_binary + i_binary
        
        output_filename = "dynamic_output.glb"
        with open(output_filename, "wb") as f:
            f.write(header + chunk_json + chunk_bin)
            
        logger.info(f"¡Geometría esculpida dinámicamente con éxito desde los píxeles!")
        return FileResponse(path=output_filename, media_type="model/gltf-binary", filename="sadv41_mesh.glb")
        
    except Exception as e:
        logger.error(f"Fallo en la escultura dinámica: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)

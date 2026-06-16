# -*- coding: utf-8 -*-
"""
Misión SADV41 — Servidor de Inferencia y Reconstrucción Geométrica
Archivo: IMAGE23D.py
Estatus: Evolución Consecutiva — Filosofía Dior
Descripción: Integra el motor de procesamiento de píxeles dinámico dentro de la
             arquitectura FastAPI consolidada que demostró estabilidad en Render.
"""

import os
import io
import struct
import logging
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image

# 1. Conservamos la estructura de Logs que ya documenta tu éxito
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [SADV41_EVO] - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="SADV41 - Motor de Inferencia Image-to-3D",
    description="Evolución unificada sobre la base operativa real.",
    version="3.1.0"
)

# 2. Mantenemos la pasarela CORS exacta que abrió la comunicación sin bloqueos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Ruta Raíz de confirmación (Health Check)
@app.get("/")
async def root_status():
    logger.info("Verificación de estado de salud del sistema.")
    return {
        "status": "online",
        "mission": "SADV41",
        "module": "IMAGE23D",
        "engine": "FastAPI Dynamic Pixel Sculptor"
    }

# 4. El Endpoint Funcional — Ahora con Cómputo Geométrico Dinámico Real
@app.post("/generate-3d/")
async def generate_3d_endpoint(file: UploadFile = File(...)):
    logger.info(f"Petición entrante validada. Nombre del recurso: {file.filename}")
    
    # Validación de formato idéntica a la anterior
    extension = os.path.splitext(file.filename)[1].lower()
    if extension not in [".jpg", ".jpeg", ".png", ".webp"]:
        logger.warning(f"Extensión rechazada: {extension}")
        raise HTTPException(
            status_code=400, 
            detail="Formato de archivo no soportado por el motor."
        )
    
    try:
        # LEER LA IMAGEN EN MEMORIA (Origen dinámico enviado desde tu celular)
        file_bytes = await file.read()
        logger.info(f"Matriz binaria leída: {len(file_bytes)} bytes.")
        
        # Procesamiento de relieve mediante escala de grises (Luminancia)
        img = Image.open(io.BytesIO(file_bytes)).convert("L")
        img = img.resize((16, 16)) # Malla optimizada de 16x16 para la CPU gratuita de Render
        
        width, height = img.size
        pixels = img.load()
        
        position_buffer = bytearray()
        index_buffer = bytearray()
        
        # ALGORITMO DE ESCULTURA (Modifica los vértices según la foto real)
        for y in range(height):
            for x in range(width):
                # Mapeo espacial normalizado de los ejes
                nx = (x / (width - 1)) - 0.5
                ny = (y / (height - 1)) - 0.5
                
                # El brillo del píxel esculpe la profundidad Z en tiempo real
                nz = (pixels[x, y] / 255.0) * 0.25
                
                # Empaquetamos la posición tridimensional como Floats de precisión (Little-Endian)
                position_buffer.extend(struct.pack('<fff', nx, nz, ny))
                
        # CONSTRUCCIÓN DE LA TOPOLOGÍA DE TRIÁNGULOS
        for y in range(height - 1):
            for x in range(width - 1):
                row1 = y * width
                row2 = (y + 1) * width
                
                v0 = row1 + x
                v1 = row1 + x + 1
                v2 = row2 + x
                v3 = row2 + x + 1
                
                # Definición de las caras de la malla indexada
                index_buffer.extend(struct.pack('<HHH', v0, v1, v2))
                index_buffer.extend(struct.pack('<HHH', v1, v3, v2))

        # Alineación de memoria para cumplir el estándar estricto de glTF/GLB
        while len(position_buffer) % 4 != 0: position_buffer.extend(b'\x00')
        while len(index_buffer) % 4 != 0: index_buffer.extend(b'\x00')
        
        pos_len = len(position_buffer)
        idx_len = len(index_buffer)
        total_bin_len = pos_len + idx_len
        
        # ESTRUCTURA JSON INTERNA DEL CONTENEDOR GLB
        json_str = (
            f'{{"asset":{{"version":"2.0"}},'
            f'"scene":0,"scenes":[{{"nodes":[0]}}],'
            f'"nodes":[{{"mesh":0}}],'
            f'"meshes":[{{"primitives":[{{"attributes":{{"POSITION":0}},"indices":1,"mode":4}}]}}],'
            f'"bufferViews":['
            f'{{"buffer":0,"byteOffset":0,"byteLength":{pos_len},"target":34962}},'
            f'{{"buffer":0,"byteOffset":{pos_len},"byteLength":{idx_len},"target":34963}}],'
            f'"buffers":[{{"byteLength":{total_bin_len}}}],'
            f'"accessors":['
            f'{{"bufferView":0,"componentType":5126,"count":{width*height},"type":"VEC3"}},'
            f'{{"bufferView":1,"componentType":5123,"count":{idx_len//2},"type":"SCALAR"}}]}}'
        )
        
        json_bytes = json_str.encode('utf-8')
        while len(json_bytes) % 4 != 0: json_bytes += b' '
        
        # ENSAMBLAJE DE LA CABECERA BINARIA FÍSICA (.GLB)
        header = struct.pack('<4sII', b'glTF', 2, 12 + 8 + len(json_bytes) + 8 + total_bin_len)
        chunk_json = struct.pack('<I4s', len(json_bytes), b'JSON') + json_bytes
        chunk_bin = struct.pack('<I4s', total_bin_len, b'BIN\x00') + position_buffer + index_buffer
        
        output_filename = "dynamic_sadv41.glb"
        with open(output_filename, "wb") as f:
            f.write(header + chunk_json + chunk_bin)
            
        logger.info("Flujo tridimensional dinámico generado y listo para despacho.")
        
        # Retorno del archivo real a través del flujo HTTP que tu mesón HTML ya sabe escuchar
        return FileResponse(
            path=output_filename, 
            media_type="model/gltf-binary", 
            filename="sadv41_mesh.glb"
        )
        
    except Exception as e:
        logger.error(f"Fallo crítico en el motor de escultura: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error en la infraestructura: {str(e)}")

# 5. Mapeo Automatizado del Puerto de Render ($PORT) que ya está verificado en verde
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    logger.info(f"Lanzando pasarela Uvicorn consolidada en el puerto: {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)

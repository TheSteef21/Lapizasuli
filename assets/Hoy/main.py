from fastapi import Form
import json
import os

ARCHIVO_JSON = "noticias.json"

@app.post("/api/actualizar")
async def agregar_noticia_dinamica(source: str = Form(...), title: str = Form(...), image: str = Form(...), time: str = Form(...)):
    # 1. Leer noticias actuales
    noticias = []
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
            try:
                noticias = json.load(f)
            except json.JSONDecodeError:
                noticias = []
                
    # 2. Crear la nueva estructura
    nueva_noticia = {
        "source": source,
        "time": time,
        "title": title,
        "image": image,
        "url": "#"
    }
    
    # 3. Insertar al inicio de la lista
    noticias.insert(0, nueva_noticia)
    
    # 4. Guardar en el archivo JSON del servidor
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=4)
        
    return {"status": "¡Noticia inyectada con éxito al Nodo SADV41!", "total_noticias": len(noticias)}

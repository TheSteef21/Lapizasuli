from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Inicialización del sistema SADV41
app = FastAPI(title="SADV41 - Algoritmo de Versículos API")

# Protección de orígenes: Solo tu GitHub Pages puede hacer peticiones aquí
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://thesteef21.github.io"], 
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api/estado-espiritual")
def obtener_estado():
    return {
        "status": "Sistema Restaurado",
        "memoria_caché": "Liberada",
        "fase_1": {
            "versiculo": "Josué 1:9",
            "accion": "Mira que te mando que te esfuerces y seas valiente; no temas ni desmayes, porque Jehová tu Dios estará contigo en dondequiera que vayas.",
            "estado": "Reinicio forzado exitoso"
        },
        "fase_2": {
            "versiculo": "Proverbios 27:17",
            "accion": "Hierro con hierro se aguza; y así el hombre aguza el rostro de su amigo.",
            "estado": "Fricción y afilado en proceso"
        },
        "mensaje_central": "El E.S. estando contigo y para ti."
    }

if __name__ == "__main__":
    # Render asigna el puerto dinámicamente, pero por defecto usamos 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)

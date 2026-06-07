from flask import Flask, request
import os
from bridge import obtener_respuesta_ia
from sender import enviar_factura_whatsapp

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    # 1. Validación inicial (GET) requerida por Meta
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        
        if mode == "subscribe" and token == os.getenv("WHATSAPP_TOKEN"):
            return challenge, 200
        return "Forbidden", 403

    # 2. Recepción y procesamiento de mensajes (POST)
    if request.method == "POST":
        data = request.json
        try:
            # Extracción del cuerpo del mensaje y el teléfono
            value = data['entry'][0]['changes'][0]['value']
            if 'messages' in value:
                mensaje = value['messages'][0]['text']['body']
                telefono = value['messages'][0]['from']
                
                # Procesar con IA (misión SADV41) y responder
                respuesta = obtener_respuesta_ia(mensaje)
                enviar_factura_whatsapp(telefono, respuesta)
                
        except (KeyError, IndexError):
            # Ignoramos mensajes que no sean de texto (ej: confirmaciones de entrega)
            pass
            
        return "OK", 200

if __name__ == "__main__":
    # Render asigna el puerto automáticamente, así que dejamos que Flask elija
    app.run()

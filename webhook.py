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
        
        # Obtenemos el token desde la variable de entorno
        stored_token = os.getenv("WHATSAPP_TOKEN")
        
        # Verificación lógica
        if mode == "subscribe" and token == stored_token:
            return challenge, 200
        else:
            print(f"Error de validación: Recibido '{token}', esperado '{stored_token}'")
            return "Forbidden", 403

    # 2. Recepción y procesamiento de mensajes (POST)
    if request.method == "POST":
        data = request.json
        try:
            value = data['entry'][0]['changes'][0]['value']
            
            # Verificamos si hay mensajes en la carga útil
            if 'messages' in value:
                # Verificamos si realmente es un mensaje de texto para evitar el KeyError
                if 'text' in value['messages'][0]:
                    mensaje = value['messages'][0]['text']['body']
                    telefono = value['messages'][0]['from']
                    
                    # Procesar con IA (Misión SADV41) y responder
                    respuesta = obtener_respuesta_ia(mensaje)
                    enviar_factura_whatsapp(telefono, respuesta)
                else:
                    # Es un evento de confirmación (leído/entregado), lo ignoramos
                    pass
        except (KeyError, IndexError) as e:
            # Capturamos el error en logs para monitoreo sin detener el servidor
            print(f"Error procesando el payload de Meta: {e}")
            pass
            
        return "OK", 200

if __name__ == "__main__":
    app.run()

from flask import Flask, request, jsonify
from bridge import obtener_respuesta_ia
from sender import enviar_factura_whatsapp

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Verificación inicial de Meta
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        return challenge if mode == "subscribe" else "Forbidden", 403

    if request.method == "POST":
        data = request.json
        # Extraer mensaje del cliente
        mensaje = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        telefono = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        
        # Procesar con IA y responder
        respuesta = obtener_respuesta_ia(mensaje)
        enviar_factura_whatsapp(telefono, respuesta)
        
        return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)


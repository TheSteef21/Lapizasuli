import os
import requests
from flask import Flask, request, jsonify
# Corregido: Importamos desde 'chiste' en singular para coincidir con tu archivo
from chistes import obtener_chiste_aleatorio

app = Flask(__name__)

@app.route('/webhook/chiste', methods=['POST'])
def enviar_contagio_humor():
    # Trigger del ecosistema
    mensaje_humor = obtener_chiste_aleatorio()
    
    # Variables de entorno para la API de Meta / WhatsApp Business
    whatsapp_url = f"https://graph.facebook.com/v17.0/{os.environ.get('WHATSAPP_BUSINESS_ACCOUNT_ID')}/messages"
    headers = {
        "Authorization": f"Bearer {os.environ.get('WHATSAPP_TOKEN')}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": os.environ.get("PHONE_NUMBER"),
        "type": "text",
        "text": {"body": mensaje_humor}
    }
    
    try:
        response = requests.post(whatsapp_url, json=payload, headers=headers, timeout=10)
        return jsonify({
            "status": "Contagio propagado con éxito", 
            "meta_response": response.json()
        }), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error al propagar en el Atrio: {e}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    # Render usa la variable PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

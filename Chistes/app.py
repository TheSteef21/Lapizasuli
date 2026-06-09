import os
import sys
import requests
from flask import Flask, request, jsonify

# Añadimos la carpeta actual al path para que encuentre chistes.py sin importar la raíz
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Ahora la importación limpia y directa funcionará a la perfección
from chistes import obtener_chiste_aleatorio

app = Flask(__name__)

@app.route('/webhook/chiste', methods=['GET', 'POST'])
def manejar_webhook_chiste():
    # 2. VERIFICACIÓN DE META (Método GET)
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        
        if mode == 'subscribe' and token == 'STEVENDIORFLOW':
            return challenge, 200
        else:
            return 'Token de verificación inválido', 403

    # 3. EJECUCIÓN DEL CONTAGIO DE HUMOR (Método POST)
    if request.method == 'POST':
        mensaje_humor = obtener_chiste_aleatorio()
        
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

# 4. CONFIGURACIÓN DE ARRANQUE PARA LOCAL O DETECCIÓN
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

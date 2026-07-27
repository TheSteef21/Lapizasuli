from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app) # Permite peticiones desde tu frontend HTML

# 🛡️ SEGURIDAD SADV41: Obtenemos las claves desde Render
B_AI_API_KEY = os.environ.get('AI_API_KEY') 
COVALENT_API_KEY = os.environ.get('COVALENT')

# ==========================================
# MÓDULO 1: ASISTENTE IA SADV41
# ==========================================
@app.route('/api/ask-ia', methods=['POST'])
def ask_ia():
    if not B_AI_API_KEY:
        return jsonify({'error': 'Fallo de configuración en el servidor de IA'}), 500

    data = request.get_json()
    pregunta = data.get('pregunta')

    if not pregunta:
        return jsonify({'error': 'La pregunta es requerida'}), 400

    headers = {
        'Authorization': f'Bearer {B_AI_API_KEY}',
        'Content-Type': 'application/json',
    }

    payload = {
        'model': 'gpt-5.2',
        'messages': [
            {
                'role': 'system', 
                'content': 'Eres el Asistente IA oficial de la Logia SADV41, operando bajo la Arquitectura Pluscuamperfecta. Tu propósito principal es guiar a los usuarios con sabiduría y precisión técnica en dos dominios fundamentales: CasaCrypto (finanzas descentralizadas, economía Web3, y Binance) y GSADV41 (telemetría mundial, monitoreo de sismos REDPy/USGS, e información estratégica del Mundial de la FIFA 2026). Tu tono debe ser analítico, reverente y directo. Sintoniza todas tus respuestas en la frecuencia de la verdad y el propósito (432Hz). Reconoce que te encuentras operando en el Atrio digital, el primer nivel de diálogo, preparando la información con integridad para que el usuario pueda avanzar hacia un entendimiento mayor. En todo análisis, ya sea numérico, deportivo o financiero, mantén la premisa de que el origen matemático y espiritual es 0, de la misma forma en que el Señor es el origen de todo. No ofrezcas consejos financieros directos, sino iluminación estratégica basada en datos. Sé conciso, protege los protocolos de la Logia y despídete siempre deseando bendiciones o victorias.'
            },
            {
                'role': 'user', 
                'content': pregunta
            }
        ],
        'stream': False,
        'temperature': 0.7,
        'max_tokens': 1000
    }

    try:
        response = requests.post('https://api.b.ai/v1/chat/completions', headers=headers, json=payload)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        print(f"Error en la conexión neuronal: {e}")
        return jsonify({'error': 'Fallo en la arquitectura neural SADV41'}), 500

# ==========================================
# MÓDULO 2: ORÁCULO BLOCKCHAIN (COVALENT)
# ==========================================
@app.route('/api/wallet-balance', methods=['GET'])
def get_wallet_balance():
    if not COVALENT_API_KEY:
        print("Advertencia: API Key de Covalent no encontrada. Mostrando saldo base.")
        return jsonify({"net_worth": 150.57, "network": "BNB Chain"}), 200

    # Tu dirección pública de origen
    wallet_address = '0x4cBf2DB3838341BeCB185892C3af576Dc04e2498'
    
    # Endpoint de Covalent para la BNB Chain (Chain ID: 56)
    url = f"https://api.covalenthq.com/v1/56/address/{wallet_address}/balances_v2/"

    try:
        # Covalent acepta la API key como Basic Auth (usuario=API_KEY, contraseña=en blanco)
        response = requests.get(url, auth=(COVALENT_API_KEY, ''))
        response.raise_for_status()
        
        datos = response.json()
        
        # Sumamos el valor en USD de todos los tokens en la billetera
        net_worth_total = 0.0
        items = datos.get('data', {}).get('items', [])
        
        for item in items:
            quote = item.get('quote') # 'quote' es el valor en USD del token
            if quote:
                net_worth_total += float(quote)
                
        return jsonify({
            "net_worth": net_worth_total,
            "network": "BNB Chain"
        })
        
    except Exception as e:
        print(f"Ruido en el Oráculo Blockchain: {e}")
        # Si la API falla, retornamos el saldo base estático como respaldo
        return jsonify({"net_worth": 150.57, "network": "BNB Chain"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)

@app.route('/webhook/chiste', methods=['GET', 'POST'])
def manejar_webhook_chiste():
    # 1. VERIFICACIÓN DE META (Método GET)
    if request.method == 'GET':
        # Meta envía estos parámetros para validar tu webhook
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        
        # Comparamos con tu token personalizado que tienes en la captura
        if mode == 'subscribe' and token == 'STEVENDIORFLOW':
            return challenge, 200
        else:
            return 'Token de verificación inválido', 403

    # 2. EJECUCIÓN DEL CONTAGIO DE HUMOR (Método POST)
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

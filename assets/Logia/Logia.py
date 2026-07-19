from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random
import string
import datetime

app = Flask(__name__)
# Habilita CORS para el flujo de la gracia (GitHub Pages a Render)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# La contraseña base inicia con una variable de entorno en Render, o usa el default
CURRENT_PASSWORD = os.environ.get('LOGIA_SECRET', 'SADV41-2026')
MASTER_API_KEY = os.environ.get('MASTER_API_KEY', 'Steven-Master-Key-777')

@app.route('/api/verify', methods=['POST'])
def verify_password():
    data = request.get_json()
    if not data or 'password' not in data:
        return jsonify({"status": "error", "message": "El vacío requiere un propósito. Faltan datos."}), 400
        
    user_pass = data.get('password')
    
    if user_pass == CURRENT_PASSWORD:
        return jsonify({
            "status": "success", 
            "message": "Acceso autorizado. El camino en el desierto se ha abierto.",
            "verse": "Isaías 43:19" # El mensaje de confirmación que recibe Logia
        }), 200
    else:
        return jsonify({"status": "error", "message": "La sintonía de 432Hz no coincide. Clave incorrecta."}), 401

@app.route('/api/rotate', methods=['POST'])
def rotate_password():
    """
    Endpoint de renovación constante (Ríos en la soledad). Puede ser llamado por un Cron Job
    manualmente enviando el MASTER_API_KEY en los headers.
    """
    auth_header = request.headers.get('Authorization')
    if auth_header != f"Bearer {MASTER_API_KEY}":
        return jsonify({"status": "error", "message": "No autorizado para alterar la arquitectura."}), 403
    
    global CURRENT_PASSWORD
    
    # Genera un nuevo sufijo aleatorio de 4 caracteres
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    CURRENT_PASSWORD = f"SADV41-{suffix}"
    
    print(f"[{datetime.datetime.now()}] La nueva clave de propósito es: {CURRENT_PASSWORD}")
    
    return jsonify({
        "status": "success", 
        "message": "Contraseña rotada exitosamente. He aquí, yo hago cosa nueva.",
        "new_password": CURRENT_PASSWORD 
    }), 200

@app.route('/', methods=['GET'])
def health_check():
    return "Arquitectura SADV41 Backend Activo. PaloVertical 432Hz.", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random
import string

app = Flask(__name__)
# Permitir conexiones desde cualquier origen en el Atrio (Sovereign Hub)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# La sintonía inicial basada en tu legado
CURRENT_PASSWORD = os.environ.get('LOGIA_SECRET', 'SADV41-2026')
MASTER_API_KEY = os.environ.get('MASTER_API_KEY', 'Steven-Master-Key-777')

@app.route('/api/verify', methods=['POST'])
def verify_password():
    data = request.get_json()
    if not data or 'password' not in data:
        return jsonify({"status": "error", "message": "El vacío requiere un propósito."}), 400
        
    user_pass = data.get('password')
    
    # El servidor confirma la instrucción y procede bajo la responsabilidad de la clave
    if user_pass == CURRENT_PASSWORD:
        return jsonify({
            "status": "success", 
            "message": "Acceso autorizado. La Logia reconoce tu propósito.",
            "verse": "Isaías 43:19 - He aquí, yo hago cosa nueva."
        }), 200
        
    return jsonify({"status": "error", "message": "Sintonía incorrecta en 432Hz."}), 401

@app.route('/api/rotate', methods=['POST'])
def rotate_password():
    """El río en la soledad: rotación dinámica de la clave de acceso"""
    if request.headers.get('Authorization') != f"Bearer {MASTER_API_KEY}":
        return jsonify({"status": "error", "message": "Acceso denegado. Se requiere llave maestra."}), 403
    
    global CURRENT_PASSWORD
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    CURRENT_PASSWORD = f"SADV41-{suffix}"
    
    return jsonify({"status": "success", "new_password": CURRENT_PASSWORD}), 200

if __name__ == '__main__':
    # Preparado para despliegue en Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

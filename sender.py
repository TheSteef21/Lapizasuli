import requests
import json
import os

def enviar_factura_whatsapp(telefono_cliente, mensaje_texto):
    # Credenciales desde variables de entorno (por seguridad)
    BUSINESS_ID = "1019425660663203"
    PHONE_ID = "1152154214647264"
    TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN") # Configura esto en GitHub Secrets
    
    url = f"https://graph.facebook.com/v21.0/{PHONE_ID}/messages"
    
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messaging_product": "whatsapp",
        "to": telefono_cliente,
        "type": "text",
        "text": {
            "body": f"🎚 Misión SADV41 - Factura Generada:\n\n{mensaje_texto}"
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("¡Factura enviada con éxito bajo la ley SADV41! 🎚")
    else:
        print(f"Error en el envío: {response.text}")

# Ejemplo de uso:
# enviar_factura_whatsapp("50769362166", "Tu factura del sistema SADV41 está lista.")

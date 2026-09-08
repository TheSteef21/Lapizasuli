import requests
import logging
import time

# 1. Configuración de Trazabilidad Forense (Logs)
# Esto guardará un registro detallado en 'auditoria_trafico.log' y en la consola.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [Acción: %(funcName)s] - %(message)s',
    handlers=[
        logging.FileHandler("auditoria_trafico.log"),
        logging.StreamHandler()
    ]
)

API_URL = "https://nolcino.com/api/v2"
# REGLA DE SEGURIDAD: Reemplaza esta variable con tu NUEVA clave generada, no la expuesta.
API_KEY = "TU_NUEVA_API_KEY_AQUI" 

def auditar_peticion(action, **kwargs):
    """
    Núcleo del simulador: Emite la petición HTTP POST y documenta la latencia 
    y el código de respuesta del servidor para análisis de bloqueos.
    """
    payload = {'key': API_KEY, 'action': action}
    payload.update(kwargs)

    # Ausencia intencional o manipulación de cabeceras para probar respuestas del WAF
    headers = {
        'User-Agent': 'Forense-Sandbox-Bot/1.0',
        'Accept': 'application/json'
    }

    logging.info(f"Iniciando inyección de petición para: {action}")
    
    try:
        start_time = time.time()
        response = requests.post(API_URL, data=payload, headers=headers)
        elapsed_time = round((time.time() - start_time) * 1000, 2)

        logging.info(f"Respuesta del servidor en {elapsed_time} ms. Código HTTP: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            logging.info(f"Carga útil (Payload) recibida: {data}")
            return data
        elif response.status_code == 429:
            logging.warning("HTTP 429 Too Many Requests: Rate Limiting activado por el servidor.")
        elif response.status_code == 403:
            logging.error("HTTP 403 Forbidden: Bloqueo algorítmico o baneo de IP detectado.")
        else:
            logging.error(f"Error anómalo del servidor: HTTP {response.status_code}")
            
        return None

    except requests.exceptions.RequestException as e:
        logging.critical(f"Fallo catastrófico en la conexión de red: {e}")
        return None

def auditar_balance():
    logging.info("--- Fase 1: Auditoría de Autenticación y Balance ---")
    return auditar_peticion('balance')

def auditar_catalogo_servicios():
    logging.info("--- Fase 2: Mapeo de Vectores de Servicio ---")
    return auditar_peticion('services')

def ejecutar_simulacion_sandbox(service_id, sandbox_url, quantity):
    """
    Fase 3: Inyección de la orden de prueba.
    ADVERTENCIA: La variable 'sandbox_url' NUNCA debe apuntar a un perfil real.
    """
    logging.info(f"--- Fase 3: Simulando Tráfico hacia {sandbox_url} ---")
    return auditar_peticion('add', service=service_id, link=sandbox_url, quantity=quantity)

if __name__ == "__main__":
    # Ejecución secuencial del entorno de pruebas
    
    # 1. Comprobar que la API key nueva funciona
    auditar_balance()
    
    # 2. Descomentar para listar los IDs de los servicios que ofrece el panel
    # auditar_catalogo_servicios()
    
    # 3. EJECUCIÓN DE PRUEBA (Reemplazar service_id con uno válido del catálogo)
    # IMPORTANTE: Utilizar una cuenta desechable (ej. una cuenta de IG o web vacía recién creada).
    # ejecutar_simulacion_sandbox(
    #     service_id=1, 
    #     sandbox_url="https://instagram.com/cuenta_falsa_de_auditoria_123", 
    #     quantity=50
    # )

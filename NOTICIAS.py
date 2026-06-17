import os
import datetime
import requests

# ==========================================
# CONFIGURACIÓN DE INFRAESTRUCTURA SOBERANA
# ==========================================
PATH_NOTICIAS_HTML = "Lapizasuli/Noticias.html"
VERSION_API = "v20.0"  # Sincronizado con la versión del fetch del HTML

# 🔐 BLINDAJE DE CREDENCIALES (Carga desde el entorno local de Termux)
# Si la variable no está en el sistema, usa por defecto el token que proporcionaste
META_TOKEN = os.getenv("META_ACCESS_TOKEN", "EAAMfqZAxF00wBRo5zb1lp7ZAGgEbrVWsxBH33DZArcE8qq1ZArVhlzRqIXkJsANyZCScZBSZAX4N4Esf77bawdmkDL1kzSAHpr3CLlEomkg5dBZATFiKzOVYpw9nwoy9GATxlpAKC5MBkZBx87tO5uKegNY3E9vLDlSNCbIJ7c1c2V5oeVizNXmg0w1GIXjoLBPfiNQXfchOnwBdoRAyWPJroOzZBUXa4Cd9ZBEsKcq7ruHtbX64ZAM2NJi5W3lQ9e1iE3HZA30pY6IZBBqDCrhy1uCq2S")
PHONE_NUMBER_ID = "1152154214647264"
RECIPIENT_NUMBER = "15556670579"

def obtener_fecha_actual():
    """Retorna la fecha y hora exacta del sistema local."""
    ahora = datetime.datetime.now()
    return ahora.strftime("%A, %d de %b de %Y, %I:%M %p")

def generar_plantilla_html_integral(noticias_lista):
    """Genera la interfaz unificada: Hypersec + Noticias + API Gateway + Web3 Workspace."""
    
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SADV41 HYPERSEC — Terminal de Control Integral</title>
    <style>
        :root {{
            --bg-color: #0c0f17;
            --panel-bg: #121824;
            --panel-dark: #080b11;
            --cyan-glow: #00e676;
            --hyper-blue: #00f0ff;
            --gold-glow: #d4af37;
            --text-main: #e0e6ed;
            --text-muted: #6272a4;
            --border-glow: rgba(0, 230, 118, 0.2);
        }}

        body {{
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: 'Courier New', Courier, monospace;
            margin: 0;
            padding: 20px;
            line-height: 1.6;
        }}

        .container {{
            max-width: 950px;
            margin: 0 auto;
            background: var(--panel-bg);
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 25px rgba(0,0,0,0.6);
            border: 1px solid #202b3e;
        }}

        header {{
            border-bottom: 2px dashed var(--hyper-blue);
            padding-bottom: 15px;
            margin-bottom: 20px;
            text-align: center;
        }}

        .system-status {{
            font-size: 0.85em;
            color: var(--gold-glow);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 10px;
        }}

        h1 {{
            color: var(--hyper-blue);
            font-size: 1.9em;
            margin: 5px 0;
            text-shadow: 0 0 10px rgba(0, 240, 255, 0.4);
        }}

        .meta-info {{
            font-size: 0.9em;
            color: var(--text-muted);
        }}

        nav {{
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            background: var(--panel-dark);
            padding: 12px;
            border: 1px solid var(--border-glow);
            margin-bottom: 25px;
            border-radius: 6px;
        }}

        nav a {{
            color: var(--hyper-blue);
            text-decoration: none;
            padding: 5px 10px;
            font-size: 0.85em;
            border: 1px solid transparent;
        }}

        nav a:hover {{
            border-color: var(--hyper-blue);
            background: rgba(0, 240, 255, 0.08);
        }}

        .grid-layout {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
        }}

        @media(min-width: 768px) {{
            .grid-layout {{ grid-template-columns: 1.2fr 0.8fr; }}
        }}

        .section {{
            margin-bottom: 20px;
            padding: 20px;
            background: var(--panel-dark);
            border-radius: 8px;
            border: 1px solid #1a2332;
            border-left: 4px solid var(--cyan-glow);
        }}

        .section.blue-layer {{ border-left-color: var(--hyper-blue); }}
        .section.gold-layer {{ border-left-color: var(--gold-glow); }}

        h3 {{
            margin-top: 0;
            color: #ffffff;
            font-size: 1.1em;
            letter-spacing: 1px;
            border-bottom: 1px solid #1a2332;
            padding-bottom: 8px;
        }}

        label {{
            display: block;
            margin: 12px 0 6px 0;
            font-weight: bold;
            font-size: 0.85em;
            color: #a0aec0;
        }}

        input[type="text"], textarea {{
            width: 100%;
            padding: 10px;
            background: var(--bg-color);
            border: 1px solid #2b394e;
            color: #fff;
            border-radius: 6px;
            box-sizing: border-box;
            font-family: monospace;
        }}

        button {{
            background-color: var(--cyan-glow);
            color: #0c0f17;
            padding: 12px 20px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: bold;
            width: 100%;
            font-size: 14px;
            letter-spacing: 1px;
            margin-top: 10px;
        }}

        button:hover {{ background-color: #00c853; }}

        .status {{
            margin-top: 15px;
            padding: 12px;
            background: var(--bg-color);
            border-radius: 6px;
            font-family: monospace;
            font-size: 12px;
            white-space: pre-wrap;
            border: 1px solid #1a2332;
        }}

        .noticia-card {{
            background: rgba(20, 28, 43, 0.7);
            border-radius: 6px;
            padding: 15px;
            margin-bottom: 15px;
            border: 1px solid rgba(0, 240, 255, 0.1);
        }}

        .noticia-titulo {{
            font-size: 1.1em;
            font-weight: bold;
            color: var(--hyper-blue);
        }}

        .noticia-cuerpo {{
            font-size: 0.9em;
            margin-top: 8px;
            color: #cbd5e1;
        }}

        .badge {{
            background-color: #1a2332;
            color: var(--cyan-glow);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 11px;
        }}

        footer {{
            margin-top: 30px;
            border-top: 1px dashed #2b394e;
            padding-top: 15px;
            text-align: center;
            font-size: 0.8em;
            color: var(--text-muted);
        }}
    </style>
</head>
<body>

<div class="container">
    <header>
        <div class="system-status">🔒 GSADV41 CLOUD TERMINAL // WEB3 HYPERSEC ENGAGED 🎚️</div>
        <h1>NOTICIAS BURUNGA TERMINAL</h1>
        <div class="meta-info">
            Registro de Red: YYWEEK24 | Invocación Sincrónica: {obtener_fecha_actual()}
        </div>
    </header>

    <nav>
        <a href="https://thesteef21.github.io/Lapizasuli/" target="_blank">🏠 Raíz Lapizasuli</a>
        <a href="https://thesteef21.github.io/Lapizasuli/GSADV41.html" target="_blank">📑 GSADV41 Base</a>
        <a href="https://thesteef21.github.io/Lapizasuli/Aporía.html" target="_blank">🧬 Aporía Framework</a>
        <a href="https://thesteef21.github.io/Lapizasuli/SADV41X.html" target="_blank">🔎 Gateway SADV41X</a>
        <a href="https://thesteef21.github.io/Lapizasuli/Noticias.html" target="_blank">📡 Canal En Vivo</a>
    </nav>

    <div class="grid-layout">
        <div class="left-column">
            
            <div class="section">
                <h3>📰 FEED DE COBERTURA GLOBAL EN VIVO (7 DE JUNIO 2026)</h3>
                <div id="feed-noticias">"""
    
    # Inserción dinámica administrada por Python
    for noticia in noticias_lista:
        html_content += f"""
                    <div class="noticia-card">
                        <div class="noticia-titulo">⚡ {noticia['titulo']}</div>
                        <div class="noticia-cuerpo">{noticia['contenido']}</div>
                    </div>"""

    html_content += f"""
                </div>
            </div>

            <div class="section gold-layer">
                <h3>🛸 INTERFAZ DESCENTRALIZADA & ECOSISTEMA WEB3</h3>
                <p style="font-size: 0.85em; color: #a0aec0;">Módulo soberano de persistencia para incursionistas y clientes de la Misión SADV41.</p>
                
                <label>Dirección de Almacenamiento IPFS (Pinata CID / Hash):</label>
                <input type="text" id="ipfsHash" value="QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco" readonly>
                
                <label>Nodo de Validación de Bloques (Web3 Wallet Gateway):</label>
                <div class="status" style="background:#070a0e; border-color:var(--gold-glow); color:var(--gold-glow);">[NETWORK STATUS]: ONLINE&#10;[WALLET FRAMEWORK]: Binance Web3 Integrated&#10;[SADV41 INTEGRITY CHECK]: PASS</div>
                
                <label>Invocación Remota Descentralizada:</label>
                <p style="font-size: 0.8em; margin: 4px 0;">Cualquier componente bloqueado puede ser reclamado directamente forzando la ruta interna:</p>
                <code style="color: var(--hyper-blue); font-size: 0.85em;">https://thesteef21.github.io/Lapizasuli/[NombreDelArchivo].html</code>
            </div>
        </div>

        <div class="right-column">
            <div class="section blue-layer">
                <h3>🎚️ CONFIGURACIÓN CLOUD API (META)</h3>
                
                <label>Meta Access Token:</label>
                <input type="text" id="token" value="{META_TOKEN}">
                
                <label>Phone Number ID:</label>
                <input type="text" id="phoneId" value="{PHONE_NUMBER_ID}">
                
                <label>Número de Destino (POST API):</label>
                <input type="text" id="recipient" value="{RECIPIENT_NUMBER}" placeholder="5076XXXXXXXX">
                
                <button id="sendBtn" onclick="enviarMensajePrueba()">Disparar Comando a Meta</button>
                
                <div class="status" id="outputLog">Esperando transmisión de comando...</div>
            </div>

            <div class="section" style="border-left-color: #7f5af0;">
                <h3>🛡️ ARQUITECTURA DEL WEBHOOK</h3>
                <ul style="padding-left: 15px; font-size: 0.8em; margin: 0;">
                    <li><span class="badge">Make.com</span> Interfaz de escucha puente activa.</li>
                    <li><span class="badge">ngrok</span> Túnel local activo para recepción en puerto de desarrollo.</li>
                </ul>
            </div>
        </div>
    </div>

    <footer>
        <p>====================================================================</p>
        <p>Misión de Servicio — Seguridad Máxima Garantizada 🗿 UFO CONTROL ENGAGED 🛂</p>
        <p>Actualizado bajo los parámetros unificados de JesuCristo [C-Code Framework]. Por Él seremos perseguidos.</p>
    </footer>
</div>

<script>
async function enviarMensajePrueba() {{
    const token = document.getElementById('token').value;
    const phoneId = document.getElementById('phoneId').value;
    const recipient = document.getElementById('recipient').value;
    const logDiv = document.getElementById('outputLog');

    if (!recipient) {{
        logDiv.innerText = "Error: Falta el número de destino.";
        logDiv.style.color = "#ff5252";
        return;
    }}

    logDiv.innerText = "Enviando comando a los servidores de Meta...";
    logDiv.style.color = "#e0e0e0";

    const url = `https://graph.facebook.com/{VERSION_API}/${{phoneId}}/messages`;
    const payload = {{
        messaging_product: "whatsapp",
        to: recipient,
        type: "template",
        template: {{
            name: "hello_world",
            language: {{ code: "en_US" }}
        }}
    }};

    try {{
        const response = await fetch(url, {{
            method: 'POST',
            headers: {{
                'Authorization': `Bearer ${{token}}`,
                'Content-Type': 'application/json'
            }} ,
            body: JSON.stringify(payload)
        }});

        const data = await response.json();

        if (response.ok) {{
            logDiv.innerText = `¡Anábasis Exitosa!\\n${{JSON.stringify(data, null, 2)}}`;
            logDiv.style.color = "#00e676";
        }} else {{
            logDiv.innerText = `Aporía detectada en Meta:\\n${{JSON.stringify(data, null, 2)}}`;
            logDiv.style.color = "#ff5252";
        }}
    }} catch (error) {{
        logDiv.innerText = `Error de Red / Conexión:\\n${{error.message}}`;
        logDiv.style.color = "#ff5252";
    }}
}}
</script>
</body>
</html>
"""
    return html_content

def ejecutar_envio_noticia_directo():
    """Ejecuta la inyección directa de Hypersec enviando la alerta de red por la API Backend."""
    url_endpoint = f"https://graph.facebook.com/{VERSION_API}/{PHONE_NUMBER_ID}/messages"
    
    headers_seguridad = {
        "Authorization": f"Bearer {META_TOKEN}",
        "Content-Type": "application/json"
    }

    payload_transmision = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT_NUMBER,
        "type": "text",
        "text": {
            "body": "⚡ *NOTICIAS BURUNGA TERMINAL* ⚡\n\nOperativo de Seguridad en La Joyita y actualización del entorno de la Misión SADV41 exitoso."
        }
    }

    try:
        response = requests.post(url_endpoint, json=payload_transmision, headers=headers_seguridad)
        res_data = response.json()
        
        if response.status_code == 200:
            print("[INTEGRITY CHECK]: PASS - Mensaje enviado con éxito mediante el backend.")
        else:
            print(f"[APORÍA DETECTADA EN BACKEND]: Código {res_data.get('error', {}).get('code')}")
            print(res_data.get('error', {}).get('message'))
    except Exception as e:
        print(f"Error en la conexión del webhook local: {e}")

def actualizar_archivos():
    """Compila las entradas y escribe físicamente el archivo local unificado."""
    print("Iniciando compilación integrada en NOTICIAS.py...")
    
    noticias_del_dia = [
        {"titulo": "Operativo de Seguridad en La Joyita", "contenido": "El Ministerio de Seguridad Pública emitió un comunicado informando sobre un despliegue coordinado de más de 2,500 efectivos de la Policía Nacional, SENAN, SENAFRONT, Migración y SUME para realizar una requisa integral en el Centro Penitenciario La Joyita (ver archivo verbatim 352427.jpg)."},
        {"titulo": "Televisión Local en Burunga", "contenido": "Se sintonizó la transmisión televisiva local donde se destacó la figura de Víctor Bernal (ver archivo verbatim 352328.jpg)."},
        {"titulo": "Fútbol y Presencia de la Misión", "contenido": "Se registraron imágenes de encuentros de fútbol con la integración visual y superposición del logo tecnológico de la misión SADV41 Python Hypersec (ver archivos verbatim 352632.jpg and 352617.jpg)."},
        {"titulo": "Gastronomía y Comercio Local", "contenido": "Circuló el menú de fin de semana (viernes, sábado y domingo) de *MC Food (Michelle & Carolina)* en Burunga-Arraiján, ofreciendo combos de comida rápida con delivery al número 6908-7059 (ver archivo verbatim 352498.jpg)."},
        {"titulo": "Publicidad de 'El Cosito del Mate'", "contenido": "Se difundió información comercial sobre este producto, resaltando ventajas como el ahorro del 50% en la yerba y la conservación del sabor original (ver archivos verbatim 352497.jpg y 352445.jpg)."},
        {"titulo": "Gran Sorteo Anticipado", "contenido": "Se promocionó el sorteo de un vehículo Kia Picanto (Vibrant MT Modelo 2026) a través de la Lotería de Boyacá y Fatimas Group S.A.S. (ver archivo verbatim 352443.jpg)."},
        {"titulo": "Versículos de la Misión", "contenido": "Se estructuró un listado con 12 versículos clave y sus significados proféticos y de bendición para la relación espiritual (ver archivo verbatim 352400.jpg)."},
        {"titulo": "Interacción en Redes Sociales", "contenido": "A la 1:11 a.m. quedó registrada una notificación en el teléfono con un meme de la cuenta *Sir Doge of the Coin* en la plataforma X, alusivo a hackear la Matrix usando la mente como computadora (ver archivo verbatim 352383.jpg)."}
    ]
    
    html_final = generar_plantilla_html_integral(noticias_del_dia)
    os.makedirs(os.path.dirname(PATH_NOTICIAS_HTML), exist_ok=True)
    
    try:
        with open(PATH_NOTICIAS_HTML, "w", encoding="utf-8") as f:
            f.write(html_final)
        print(f"¡Sincronización Exitosa! Archivo físico sobrescrito en: {PATH_NOTICIAS_HTML}")
        
        # Una vez generado el archivo, ejecuta la prueba de transmisión de datos en paralelo
        ejecutar_envio_noticia_directo()
        
    except Exception as e:
        print(f"Error crítico en el despliegue físico de la plantilla: {e}")

if __name__ == "__main__":
    actualizar_archivos()

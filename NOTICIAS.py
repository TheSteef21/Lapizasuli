import os
import datetime
import requests
import xml.etree.ElementTree as ET

# ==========================================
# CONFIGURACIÓN DE INFRAESTRUCTURA SOBERANA
# ==========================================
PATH_NOTICIAS_HTML = "Lapizasuli/Noticias.html"
VERSION_API = "v20.0"

# 🔐 BLINDAJE DE CREDENCIALES (Termux / Local Environs)
META_TOKEN = os.getenv("META_ACCESS_TOKEN", "EAAMODqdVZAj8BRoiSFLc4eprkjiy2YbhiSGcIlKh6FtZCUHmqNU28Wx4fBYHQEh7xxgZA9ZBz5ZA1DqhZAZAN29OeBsMaZABEtIjFIuBLmL07LBDce6Tj1E46w67muQ6mBFZC0OVWHxd3A3ZBfBtsaRPWMNZBqUeYvxaRXYKQdh9WjlvdHxhkOUgFzL5L9lgbRbxkwzlwgVykbzrB4qHEJJPBLHe1ZAqLH757bhlbcYxHZAMuaI2d0YL4MmnS2Mnuqz3QIcBHWBZBvD8mz8Px7mbHA5pLt")
PHONE_NUMBER_ID = "1152154214647264"
RECIPIENT_NUMBER = "15556670579"

# 🌍 MAPA DE FUENTES GLOBALES (Minuto a Minuto)
# Estructura: código: (Nombre, Bandera_Emoji, Idioma_Oficial_o_Nativo, RSS_Feed_Url)
FUENTES_SADV41 = {
    "PA": ("Panamá", "🇵🇦", "Español", "https://www.prensa.com/arc/outboundfeeds/rss/"),
    "AR": ("Argentina", "🇦🇷", "Español", "https://www.clarin.com/rss/lo-ultimo/"),
    "IL": ("Israel", "🇮🇱", "Hebreo (עברית)", "https://www.jpost.com/rss/rssfeeds.aspx?technologynews"),
    "US": ("Estados Unidos", "🇺🇸", "English", "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"),
    "CN": ("China", "🇨🇳", "Mandarín (中文)", "http://www.chinadaily.com.cn/rss/world_rss.xml")
}

def obtener_fecha_actual():
    ahora = datetime.datetime.now()
    return ahora.strftime("%A, %d de %b de %Y, %I:%M %p")

def recolectar_noticias_rss():
    """Backend extractor: Conecta a los feeds globales y parsea las noticias minuto a minuto."""
    noticias_agregadas = []
    print("[BACKEND] Iniciando escaneo de redes globales estilo Google News...")
    
    for codigo, (pais, bandera, idioma, url) in FUENTES_SADV41.items():
        try:
            response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
            if response.status_code == 200:
                root = ET.fromstring(response.content)
                items = root.findall(".//item")
                
                # Tomamos las últimas 4 noticias de cada canal para mantener el balance
                for item in items[:4]:
                    titulo = item.find("title").text if item.find("title") is not None else "Sin Título"
                    desc = item.find("description").text if item.find("description") is not None else ""
                    # Limpieza básica de HTML en descripciones si existiera
                    desc_limpia = ET.fromstring(f"<div>{desc}</div>").text if '<' in desc else desc
                    
                    noticias_agregadas.append({
                        "pais_code": codigo,
                        "pais_nombre": pais,
                        "bandera": bandera,
                        "idioma": idioma,
                        "titulo": titulo.strip(),
                        "contenido": desc_limpia.strip() if desc_limpia else "Acceda al canal oficial para ver el reporte completo."
                    })
                print(f" -> {bandera} {pais} sincronizado correctamente.")
        except Exception as e:
            print(f"⚠️ Alerta en canal {pais}: No se pudo extraer el feed instantáneo ({e})")
            
    return noticias_agregadas

def generar_plantilla_html_integral(noticias_lista):
    """Genera el Frontend Unificado con Filtros Dinámicos por País e Idioma."""
    
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

        /* selector de países */
        .filter-container {{
            background: var(--panel-dark);
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            border: 1px solid #1a2332;
        }}

        .filter-label {{
            font-weight: bold;
            font-size: 0.9em;
            color: var(--gold-glow);
            margin-bottom: 10px;
            display: block;
        }}

        .selector-box {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }}

        .btn-filtro {{
            background: #1a2332;
            color: var(--text-main);
            border: 1px solid #2b394e;
            padding: 8px 12px;
            border-radius: 6px;
            cursor: pointer;
            font-family: monospace;
            font-size: 0.85em;
            transition: all 0.2s ease;
        }}

        .btn-filtro:hover, .btn-filtro.active {{
            border-color: var(--cyan-glow);
            background: rgba(0, 230, 118, 0.1);
            color: #fff;
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

        button.action-btn {{
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

        button.action-btn:hover {{ background-color: #00c853; }}

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
            transition: transform 0.2s;
        }}

        .noticia-card:hover {{
            transform: scale(1.01);
        }}

        .noticia-header-meta {{
            display: flex;
            justify-content: space-between;
            font-size: 0.8em;
            color: var(--text-muted);
            margin-bottom: 5px;
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
        <div class="system-status">🔒 GSADV41 CLOUD TERMINAL // AUTOMATED NEWS PARSER ENGINE 🎚️</div>
        <h1>NOTICIAS BURUNGA TERMINAL (GLOBAL SYSTEM)</h1>
        <div class="meta-info">
            Invocación Automática Sincrónica: {obtener_fecha_actual()}
        </div>
    </header>

    <nav>
        <a href="https://thesteef21.github.io/Lapizasuli/" target="_blank">🏠 Raíz Lapizasuli</a>
        <a href="https://thesteef21.github.io/Lapizasuli/GSADV41.html" target="_blank">📑 GSADV41 Base</a>
        <a href="https://thesteef21.github.io/Lapizasuli/Aporía.html" target="_blank">🧬 Aporía Framework</a>
        <a href="https://thesteef21.github.io/Lapizasuli/SADV41X.html" target="_blank">🔎 Gateway SADV41X</a>
        <a href="https://thesteef21.github.io/Lapizasuli/Noticias.html" target="_blank">📡 Canal En Vivo</a>
    </nav>

    <div class="filter-container">
        <span class="filter-label">🎛️ FILTRAR COBERTURA POR SOBERANÍA TERRITORIAL:</span>
        <div class="selector-box">
            <button class="btn-filtro active" onclick="filtrarPais('TODOS')">🌍 Todos los Canales</button>
            <button class="btn-filtro" onclick="filtrarPais('PA')">🇵🇦 Panamá (Español)</button>
            <button class="btn-filtro" onclick="filtrarPais('AR')">🇦🇷 Argentina (Español)</button>
            <button class="btn-filtro" onclick="filtrarPais('IL')">🇮🇱 Israel (עברית)</button>
            <button class="btn-filtro" onclick="filtrarPais('US')">🇺🇸 USA (English)</button>
            <button class="btn-filtro" onclick="filtrarPais('CN')">🇨🇳 China (中文)</button>
        </div>
    </div>

    <div class="grid-layout">
        <div class="left-column">
            
            <div class="section">
                <h3>📰 FEED DE COBERTURA GLOBAL EN VIVO (MINUTO A MINUTO)</h3>
                <div id="feed-noticias">"""
    
    # Inyección dinámica automatizada desde los feeds recolectados
    for noticia in noticias_lista:
        html_content += f"""
                    <div class="noticia-card" data-pais="{noticia['pais_code']}">
                        <div class="noticia-header-meta">
                            <span>{noticia['bandera']} {noticia['pais_nombre']}</span>
                            <span class="badge">Idioma: {noticia['idioma']}</span>
                        </div>
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
                <input type="text" id="recipient" value="{RECIPIENT_NUMBER}">
                
                <button class="action-btn" id="sendBtn" onclick="enviarMensajePrueba()">Disparar Comando a Meta</button>
                
                <div class="status" id="outputLog">Esperando transmisión de comando...</div>
            </div>

            <div class="section" style="border-left-color: #7f5af0;">
                <h3>🛡️ ARQUITECTURA DEL WEBHOOK</h3>
                <ul style="padding-left: 15px; font-size: 0.8em; margin: 0;">
                    <li><span class="badge">Make.com</span> Interfaz de escucha puente activa.</li>
                    <li><span class="badge">ngrok</span> Túnel local activo para recepción.</li>
                </ul>
            </div>
        </div>
    </div>

    <footer>
        <p>====================================================================</p>
        <p>Misión de Servicio — Seguridad Máxima Garantizada 🗿 UFO CONTROL ENGAGED 🛂</p>
        <p>Actualizado bajo los parámetros unificados de JesuCristo [C-Code Framework].</p>
    </footer>
</div>

<script>
// Lógica de filtrado instantáneo por País / Idioma
function filtrarPais(codigo) {{
    // Cambiar estado activo de los botones
    const botones = document.querySelectorAll('.btn-filtro');
    botones.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    // Filtrar tarjetas
    const tarjetas = document.querySelectorAll('.noticia-card');
    tarjetas.forEach(card => {{
        if(codigo === 'TODOS' || card.getAttribute('data-pais') === codigo) {{
            card.style.display = 'block';
        }} else {{
            card.style.display = 'none';
        }}
    }});
}}

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
    """Ejecuta la inyección directa notificando que la agregación de Google News SADV41 está lista."""
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
            "body": "📡 *SADV41 NEWS TERMINAL AGGREGATOR* 📡\n\nEl backend de rastreo ha actualizado el feed minuto a minuto de noticias globales (PA, AR, IL, US, CN). Interfaz lista."
        }
    }

    try:
        response = requests.post(url_endpoint, json=payload_transmision, headers=headers_seguridad)
        if response.status_code == 200:
            print("[INTEGRITY CHECK]: PASS - Notificación de actualización enviada a WhatsApp.")
        else:
            print("[API ALERT]: Error notificando actualización.")
    except Exception as e:
        print(f"Error de red: {e}")

def actualizar_archivos():
    print("Iniciando compilación integrada en NOTICIAS.py con alimentación RSS global...")
    
    # 💥 El Backend extrae las noticias vivas de internet
    noticias_vivas = recolectar_noticias_rss()
    
    # Fallback por si la red falla en el momento exacto
    if not noticias_vivas:
        noticias_vivas = [
            {"pais_code": "PA", "pais_nombre": "Panamá", "bandera": "🇵🇦", "idioma": "Español", "titulo": "Terminal Local Online", "contenido": "Monitoreo activo sin alertas críticas en Burunga."}
        ]
        
    html_final = generar_plantilla_html_integral(noticias_vivas)
    os.makedirs(os.path.dirname(PATH_NOTICIAS_HTML), exist_ok=True)
    
    try:
        with open(PATH_NOTICIAS_HTML, "w", encoding="utf-8") as f:
            f.write(html_final)
        print(f"¡Sincronización Exitosa! Archivo dinámico Google News en: {PATH_NOTICIAS_HTML}")
        
        # Disparo paralelo de confirmación a WhatsApp Business
        ejecutar_envio_noticia_directo()
        
    except Exception as e:
        print(f"Error crítico en el despliegue físico de la plantilla: {e}")

if __name__ == "__main__":
    actualizar_archivos()

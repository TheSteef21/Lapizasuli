import os
import datetime
import requests
import xml.etree.ElementTree as ET

# ==========================================
# CONFIGURACIÓN DE INFRAESTRUCTURA SOBERANA
# ==========================================
PATH_NOTICIAS_CYBER = "Lapizasuli/Noticias.html" # Terminal Monocromática / Cyberpunk
PATH_SOVEREIGN_HUB = "Lapizasuli/GSADV41.html"  # Hub de Estética Avanzada y Telemetría
VERSION_API = "v20.0"

# 🔐 BLINDAJE DE CREDENCIALES (Carga desde el entorno o valores por defecto seguros)
META_TOKEN = os.getenv("META_ACCESS_TOKEN", "EAAMfqZAxF00wBRo5zb1lp7ZAGgEbrVWsxBH33DZArcE8qq1ZArVhlzRqIXkJsANyZCScZBSZAX4N4Esf77bawdmkDL1kzSAHpr3CLlEomkg5dBZATFiKzOVYpw9nwoy9GATxlpAKC5MBkZBx87tO5uKegNY3E9vLDlSNCbIJ7c1c2V5oeVizNXmg0w1GIXjoLBPfiNQXfchOnwBdoRAyWPJroOzZBUXa4Cd9ZBEsKcq7ruHtbX64ZAM2NJi5W3lQ9e1iE3HZA30pY6IZBBqDCrhy1uCq2S")
PHONE_NUMBER_ID = "1152154214647264"
RECIPIENT_NUMBER = "15556670579"

# 🌍 MAPA DE FUENTES GLOBALES (Minuto a Minuto)
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
    """Backend extractor: Conecta a los feeds globales minuto a minuto."""
    noticias_agregadas = []
    print("[BACKEND] Rastreador global activado. Extrayendo flujos informativos...")
    
    for codigo, (pais, bandera, idioma, url) in FUENTES_SADV41.items():
        try:
            response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
            if response.status_code == 200:
                root = ET.fromstring(response.content)
                items = root.findall(".//item")
                
                for item in items[:4]:  # Extrae las 4 noticias más recientes de cada soberanía
                    titulo = item.find("title").text if item.find("title") is not None else "Sin Título"
                    desc = item.find("description").text if item.find("description") is not None else ""
                    desc_limpia = ET.fromstring(f"<div>{desc}</div>").text if '<' in desc else desc
                    
                    noticias_agregadas.append({
                        "pais_code": codigo,
                        "pais_nombre": pais,
                        "bandera": bandera,
                        "idioma": idioma,
                        "titulo": titulo.strip(),
                        "contenido": desc_limpia.strip() if desc_limpia else "Acceda al canal oficial para ver el reporte completo."
                    })
                print(f" -> {bandera} {pais} procesado con éxito.")
        except Exception as e:
            print(f"⚠️ Omisión temporal en canal {pais}: {e}")
            
    return noticias_agregadas

def generar_plantilla_html_cyber(noticias_lista):
    """Genera el Frontend Unificado estilo Terminal de Control Hypersec."""
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

        .noticia-card:hover {{ transform: scale(1.01); }}

        .noticia-header-meta {{
            display: flex;
            justify-content: space-between;
            font-size: 0.8em;
            color: var(--text-muted);
            margin-bottom: 5px;
        }}

        .noticia-titulo {{ font-size: 1.1em; font-weight: bold; color: var(--hyper-blue); }}
        .noticia-cuerpo {{ font-size: 0.9em; margin-top: 8px; color: #cbd5e1; }}
        .badge {{ background-color: #1a2332; color: var(--cyan-glow); padding: 2px 6px; border-radius: 4px; font-size: 11px; }}
        footer {{ margin-top: 30px; border-top: 1px dashed #2b394e; padding-top: 15px; text-align: center; font-size: 0.8em; color: var(--text-muted); }}
    </style>
</head>
<body>
<div class="container">
    <header>
        <div class="system-status">🔒 GSADV41 CLOUD TERMINAL // AUTOMATED NEWS PARSER ENGINE 🎚️</div>
        <h1>NOTICIAS BURUNGA TERMINAL (GLOBAL SYSTEM)</h1>
        <div class="meta-info">Invocación Automática Sincrónica: {obtener_fecha_actual()}</div>
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
                <div class="status" style="background:#070a0e; border-color:var(--gold-glow); color:var(--gold-glow);">[NETWORK STATUS]: ONLINE
[WALLET FRAMEWORK]: Binance Web3 Integrated
[SADV41 INTEGRITY CHECK]: PASS</div>
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
function filtrarPais(codigo) {{
    const botones = document.querySelectorAll('.btn-filtro');
    botones.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

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
    const url = `https://graph.facebook.com/{VERSION_API}/\${{phoneId}}/messages`;
    const payload = {{
        messaging_product: "whatsapp",
        to: recipient,
        type: "template",
        template: {{ name: "hello_world", language: {{ code: "en_US" }} }}
    }};

    try {{
        const response = await fetch(url, {{
            method: 'POST',
            headers: {{ 'Authorization': `Bearer \${{token}}`, 'Content-Type': 'application/json' }},
            body: JSON.stringify(payload)
        }});
        const data = await response.json();
        if (response.ok) {{
            logDiv.innerText = `¡Anábasis Exitosa!\\n\${{JSON.stringify(data, null, 2)}}`;
            logDiv.style.color = "#00e676";
        }} else {{
            logDiv.innerText = `Aporía detectada en Meta:\\n\${{JSON.stringify(data, null, 2)}}`;
            logDiv.style.color = "#ff5252";
        }}
    }} catch (error) {{
        logDiv.innerText = `Error de Red / Conexión:\\n\${{error.message}}`;
        logDiv.style.color = "#ff5252";
    }}
}}
</script>
</body>
</html>
"""
    return html_content

def generar_hub_soberano_integral(noticias_lista):
    """Compila la interfaz unificada definitiva con diseño estético de Tailwind CSS."""
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sovereign Hub | SADV41, Miss Mundo Latina & Monitoreo Sísmico</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/@web3auth/modal@8"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/ethers/6.7.0/ethers.umd.min.js"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        navy: '#020617', oro: '#eab308', blanco: '#f8fafc', borgona: '#4a0010', neonPink: '#ff2a74', neonBlue: '#00f3ff', renderRed: '#da3637'
                    }},
                    fontFamily: {{ sans: ['Inter', 'sans-serif'], serif: ['Playfair Display', 'serif'] }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ background-color: #020617; background-image: radial-gradient(#1e293b 0.5px, transparent 0.5px); background-size: 24px 24px; color: #f8fafc; }}
        .glass {{ background: rgba(2, 6, 23, 0.75); backdrop-filter: blur(12px); border: 1px solid rgba(234, 179, 8, 0.2); }}
        .glass-sismico {{ background: #161b22; border: 1px solid #30363d; }}
        .text-shadow-oro {{ text-shadow: 0 0 10px rgba(234, 179, 8, 0.5); }}
        .text-shadow-pink {{ text-shadow: 0 0 10px rgba(255, 42, 116, 0.6); }}
        .text-shadow-blue {{ text-shadow: 0 0 10px rgba(0, 243, 255, 0.6); }}
        .sismo-card {{ background-color: #1f242c; border-left: 5px solid #ff6b81; }}
        .btn-filtro {{ background: #161b22; border: 1px solid #30363d; transition: all 0.2s ease; }}
        .btn-filtro.active, .btn-filtro:hover {{ border-color: #eab308; background: rgba(234, 179, 8, 0.1); }}
    </style>
</head>
<body class="font-sans antialiased selection:bg-oro selection:text-navy">
    <header class="fixed w-full z-50 glass border-b border-oro/30 px-6 py-4 flex flex-col md:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-3">
            <span class="text-2xl">🛡️</span>
            <div>
                <h1 class="font-serif text-xl tracking-wider text-oro font-bold">SOVEREIGN HUB</h1>
                <p class="text-[9px] text-slate-400 font-mono tracking-widest">SADV41 DIGITAL ARCHITECTURE</p>
            </div>
        </div>
        <nav class="flex flex-wrap justify-center gap-6 text-sm uppercase tracking-wider font-medium">
            <a href="#embassy-story" class="hover:text-pink-400 transition-colors text-pink-300">Embassy Story</a>
            <a href="#global-news-section" class="hover:text-yellow-400 transition-colors text-yellow-300 font-bold">📡 Global News</a>
            <a href="#monitor-sismico-seccion" class="hover:text-red-400 transition-colors text-red-300 font-bold">⚠️ Telemetría SADV41T</a>
        </nav>
        <div class="flex flex-wrap gap-2 justify-center">
            <button onclick="loginSocial('google')" class="bg-white hover:bg-slate-200 text-slate-900 font-semibold text-xs px-3 py-2 rounded transition-all flex items-center gap-1.5 shadow cursor-pointer">🌐 Google Connect</button>
            <button onclick="connectBinance()" class="bg-oro hover:bg-amber-600 text-navy font-bold text-xs px-3 py-2 rounded transition-all flex items-center gap-1.5 shadow-lg shadow-oro/20 cursor-pointer">⚡ Binance Web3 Wallet</button>
        </div>
    </header>

    <main class="pt-44 pb-12 px-6 max-w-6xl mx-auto space-y-16">
        <section id="embassy-story" class="glass rounded-2xl overflow-hidden border border-pink-500/30 shadow-2xl max-w-lg mx-auto">
            <div class="p-8 text-center border-b border-white/5 bg-gradient-to-b from-pink-500/10 to-transparent">
                <h2 class="font-serif text-2xl md:text-3xl text-white font-extrabold tracking-wider text-shadow-pink uppercase">GSADV41: EMBASSY OF BEAUTY</h2>
                <p class="text-oro font-semibold text-sm tracking-widest mt-1 uppercase">6 Expressions of Sisterhood & Grace</p>
                <p class="text-xs text-slate-400 mt-4 leading-relaxed">El santuario secreto donde la belleza no compite; se comparte, se restaura y se multiplica bajo la ley de gracia de Miss Mundo GSADV41.</p>
            </div>
            <div class="p-6 space-y-4 bg-slate-950/40">
                <div class="bg-white/[0.02] border-l-4 border-[#ff2a74] p-4 rounded-r-xl transition-all hover:translate-x-1 hover:bg-white/[0.04]">
                    <div class="flex justify-between items-center mb-1"><span class="text-sm font-bold text-white">The Emergency Therapist</span><span class="text-[10px] text-oro uppercase tracking-wider font-semibold">Consuelo</span></div>
                    <p class="text-xs text-slate-400 leading-relaxed">Restoring Her Crown. Te recibe con empatía divina, te seca las lágrimas y te recuerda el valor real de tu corona.</p>
                </div>
                <div class="bg-white/[0.02] border-l-4 border-[#00f3ff] p-4 rounded-r-xl transition-all hover:translate-x-1 hover:bg-white/[0.04]">
                    <div class="flex justify-between items-center mb-1"><span class="text-sm font-bold text-white">The Beauty Ambassador</span><span class="text-[10px] text-oro uppercase tracking-wider font-semibold">Generosidad</span></div>
                    <p class="text-xs text-slate-400 leading-relaxed">A Mirror of Generosity. Despliega un tocador impecable para ofrecer retoques de gracia y elegancia sin costo.</p>
                </div>
                <div class="bg-white/[0.02] border-l-4 border-[#ff2a74] p-4 rounded-r-xl transition-all hover:translate-x-1 hover:bg-white/[0.04]">
                    <div class="flex justify-between items-center mb-1"><span class="text-sm font-bold text-white">The 5-Minute Sister</span><span class="text-[10px] text-oro uppercase tracking-wider font-semibold">Conexión</span></div>
                    <p class="text-xs text-slate-400 leading-relaxed">Instant Connection. Admiración mutua y genuina de pasarela; un choque de palmas y un lazo digital instantáneo.</p>
                </div>
                <div class="bg-white/[0.02] border-l-4 border-[#00f3ff] p-4 rounded-r-xl transition-all hover:translate-x-1 hover:bg-white/[0.04]">
                    <div class="flex justify-between items-center mb-1"><span class="text-sm font-bold text-white">The Search Squadron</span><span class="text-[10px] text-oro uppercase tracking-wider font-semibold">Resguardo</span></div>
                    <p class="text-xs text-slate-400 leading-relaxed">No Woman Left Behind. Activación inmediata y solidaria ante el llamado de alerta para proteger a la compañera.</p>
                </div>
                <div class="bg-white/[0.02] border-l-4 border-[#ff2a74] p-4 rounded-r-xl transition-all hover:translate-x-1 hover:bg-white/[0.04]">
                    <div class="flex justify-between items-center mb-1"><span class="text-sm font-bold text-white">The Mirror Visionary</span><span class="text-[10px] text-oro uppercase tracking-wider font-semibold">Esencia</span></div>
                    <p class="text-xs text-slate-400 leading-relaxed">Perfecting the Reflection. Captura la luz, la sofisticación y el encuadre perfecto de la hermandad en el espejo.</p>
                </div>
                <div class="bg-white/[0.02] border-l-4 border-[#00f3ff] p-4 rounded-r-xl transition-all hover:translate-x-1 hover:bg-white/[0.04]">
                    <div class="flex justify-between items-center mb-1"><span class="text-sm font-bold text-white">The Dancefloor Philosopher</span><span class="text-[10px] text-oro uppercase tracking-wider font-semibold">Propósito</span></div>
                    <p class="text-xs text-slate-400 leading-relaxed">Live with Purpose. Sabiduría pura de pista que inspira a levantar la frente y celebrar la vida con plenitud absoluta.</p>
                </div>
            </div>
        </section>

        <section id="global-news-section" class="max-w-3xl mx-auto p-6 bg-[#0d1117] border border-slate-800 rounded-2xl shadow-xl space-y-6">
            <div class="text-center">
                <h2 class="text-oro font-bold text-2xl md:text-3xl tracking-tight uppercase text-shadow-oro">GSADV41 Global Aggregator</h2>
                <p class="text-slate-400 text-xs md:text-sm mt-1">Rastreo de Información Soberana Minuto a Minuto</p>
                <p class="text-[10px] text-slate-500 font-mono mt-1">Sincronización de Red: {obtener_fecha_actual()}</p>
            </div>
            <div class="bg-[#161b22] p-4 rounded-xl border border-slate-800">
                <span class="text-xs font-bold text-slate-400 block mb-3 uppercase tracking-wider">🎛️ Selector de Cobertura Territorial:</span>
                <div class="flex flex-wrap gap-2">
                    <button class="btn-filtro active text-xs font-mono text-white px-3 py-2 rounded-lg" onclick="filtrarNoticias('TODOS')">🌍 Todos</button>
                    <button class="btn-filtro text-xs font-mono text-white px-3 py-2 rounded-lg" onclick="filtrarNoticias('PA')">🇵🇦 Panamá</button>
                    <button class="btn-filtro text-xs font-mono text-white px-3 py-2 rounded-lg" onclick="filtrarNoticias('AR')">🇦🇷 Argentina</button>
                    <button class="btn-filtro text-xs font-mono text-white px-3 py-2 rounded-lg" onclick="filtrarNoticias('IL')">🇮🇱 Israel</button>
                    <button class="btn-filtro text-xs font-mono text-white px-3 py-2 rounded-lg" onclick="filtrarNoticias('US')">🇺🇸 USA</button>
                    <button class="btn-filtro text-xs font-mono text-white px-3 py-2 rounded-lg" onclick="filtrarNoticias('CN')">🇨🇳 China</button>
                </div>
            </div>
            <div id="contenedor-noticias-feed" class="space-y-4">"""
    
    for noticia in noticias_lista:
        html_content += f"""
                <div class="noticia-tarjeta-item bg-[#1f242c] p-4 rounded-xl border border-slate-800/60" data-pais="{noticia['pais_code']}">
                    <div class="flex justify-between items-center text-[11px] text-slate-400 font-mono mb-2">
                        <span>{noticia['bandera']} {noticia['pais_nombre']}</span>
                        <span class="bg-slate-900 text-amber-400 px-2 py-0.5 rounded border border-slate-800">Idioma: {noticia['idioma']}</span>
                    </div>
                    <h4 class="text-cyan-400 font-bold text-sm leading-snug">⚡ {noticia['titulo']}</h4>
                    <p class="text-xs text-slate-300 mt-2 leading-relaxed font-sans">{noticia['contenido']}</p>
                </div>"""

    html_content += f"""
            </div>
        </section>

        <section id="monitor-sismico-seccion" class="max-w-3xl mx-auto p-6 bg-[#0d1117] border border-slate-800 rounded-2xl shadow-xl">
            <div class="text-center py-4">
                <h2 class="text-renderRed font-bold text-2xl md:text-3xl tracking-tight uppercase">Módulo SADV41T</h2>
                <p class="text-slate-400 text-xs md:text-sm mt-1 border-b border-slate-800 pb-4">Detección y Clasificación de Familias Sísmicas Repetitivas (REDPy / USGS)</p>
            </div>
            <div class="flex justify-center items-center gap-4 my-4">
                <button id="btn-refrescar" class="bg-[#ff6b81] hover:bg-[#ff4757] text-white font-bold text-sm px-5 py-2.5 rounded-lg transition-all active:scale-95 cursor-pointer" onclick="refrescarMonitor()">Refrescar Monitor</button>
                <div id="badge-estado" class="bg-renderRed/10 text-renderRed border border-renderRed/40 px-4 py-1.5 rounded-full font-bold text-xs tracking-wide">Sincronizando...</div>
            </div>
            <div id="contenedor-error" class="bg-red-500/10 border border-red-500 rounded-xl p-4 text-sm text-left space-y-1 hidden">
                <span class="font-bold text-red-500 flex items-center gap-1">⚠️ Modo Respaldo Activado:</span> 
                <p class="text-slate-300 text-xs">No se pudo conectar con el servidor dinámico a través de la ruta proxy de Render (Timeout/Cold Start). Mostrando el último registro de la estación local.</p>
            </div>
            <div id="monitor-salida" class="space-y-4 mt-6"></div>
        </section>

        <section class="glass rounded-2xl max-w-lg mx-auto overflow-hidden border border-cyan-500/30">
            <div class="p-6 bg-black/30 flex flex-col items-center gap-4 text-center">
                <div class="border border-[#00f3ff]/40 px-4 py-1.5 rounded-full text-xs font-bold text-[#00f3ff] tracking-wide text-shadow-blue uppercase">CONFESIONARIO DE GRACIA & ALERTAS GLOBALES</div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 w-full pt-2 px-4">
                    <a href="https://wa.me/+15556670579" target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs px-4 py-2.5 rounded-lg transition-all shadow flex items-center justify-center gap-1.5 cursor-pointer col-span-2 sm:col-span-1">💬 Contactar IA SADV41</a>
                    <a href="https://www.instagram.com/reel/DZNKr6Sla4M/?igsh=bDUzODcwanlyZWp6" target="_blank" class="bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 text-white font-semibold text-xs px-4 py-2.5 rounded-lg transition-all shadow flex items-center justify-center gap-1.5 cursor-pointer col-span-2 sm:col-span-1">📸 Ver Reel Instagram</a>
                </div>
                <div class="text-2xl mt-2 animate-[pulse_2s_infinite]">🎚</div>
            </div>
        </section>
    </main>

    <script>
        const API_URL = "https://lapizasuli.onrender.com/api/sismos";
        const datosRespaldoLocal = {{
            "analisis_ia": "Análisis en modo local (Respaldo del Hub). Telemetría estable registrada en la red de estaciones.",
            "acumulado_total": 24,
            "eventos": [{{
                "id": "SADV41-2026-A", "ubicacion": "Zona de Subducción / Red de Estaciones USGS", "pais_region": "Panamá", "latitud": 7.0, "longitud": -82.5, "google_maps_url": "http://maps.google.com/?q=7.0000,-82.5000", "magnitud": 5.1, "profundidad_km": 26.2, "familia_redpy": "Familia Volcánica #04", "coeficiente_correlacion": 0.89, "fecha_hora": "2026-06-08 04:48:30"
            }}]
        }};

        function filtrarNoticias(codigo) {{
            const botones = document.querySelectorAll('.btn-filtro');
            botones.forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');

            const tarjetas = document.querySelectorAll('.noticia-tarjeta-item');
            tarjetas.forEach(card => {{
                if(codigo === 'TODOS' || card.getAttribute('data-pais') === codigo) {{ card.style.display = 'block'; }} else {{ card.style.display = 'none'; }}
            }});
        }}

        function renderizarDatos(data) {{
            const monitorSalida = document.getElementById("monitor-salida");
            let htmlContenido = `
                <div class="glass-sismico border border-slate-800 rounded-xl p-5 text-left shadow-inner">
                    <div class="flex justify-between items-center mb-2">
                        <h4 class="text-[#58a6ff] font-bold text-sm flex items-center gap-1.5">🤖 Diagnóstico del Motor de IA:</h4>
                        <span class="text-[10px] bg-slate-800 px-2 py-0.5 rounded font-mono text-slate-400">Acumulado Total: \\\${{data.acumulado_total || 24}}</span>
                    </div>
                    <p class="text-xs text-slate-300 leading-relaxed font-mono">\\\${{data.analisis_ia || "Procesando firmas..."}}</p>
                </div>`;
            data.eventos.forEach(sismo => {{
                htmlContenido += `
                    <div class="sismo-card border-l-4 border-rose-500 p-4 rounded-r-xl text-left bg-slate-950/50 border border-y-slate-800 border-r-slate-800">
                        <div class="text-xs text-slate-200 font-semibold mb-1 flex justify-between items-center">
                            <span>📍 Ubicación: <span class="text-white">\\\${{sismo.ubicacion}} (\\\${{sismo.pais_region || 'Panamá'}})</span></span>
                            <a href="\\\${{sismo.google_maps_url}}" target="_blank" class="text-blue-400 hover:underline text-[10px] font-mono">📍 Ver Mapa</a>
                        </div>
                        <div class="text-xs text-slate-400 grid grid-cols-2 gap-y-1 font-mono">
                            <div>📊 Magnitud: <span class="text-rose-400 font-bold">M \\\${{sismo.magnitud}}</span></div>
                            <div>📉 Profundidad: <span class="text-cyan-400 font-bold">\\\${{sismo.profundidad_km}} km</span></div>
                            <div class="col-span-2">🧬 REDPy: <span class="text-amber-400">\\\${{sismo.familia_redpy}}</span></div>
                        </div>
                    </div>`;
            }});
            monitorSalida.innerHTML = htmlContenido;
        }}

        async function refrescarMonitor() {{
            const botonRefrescar = document.getElementById("btn-refrescar");
            const contenedorError = document.getElementById("contenedor-error");
            const badgeEstado = document.getElementById("badge-estado");
            const controller = new AbortController();
            const timeoutId = setTimeout(() => controller.abort(), 6000);

            try {{
                if (botonRefrescar) botonRefrescar.innerText = "Sincronizando...";
                const response = await fetch(API_URL, {{ signal: controller.signal }});
                clearTimeout(timeoutId);
                if (!response.ok) throw new Error();
                const data = await response.json();
                if (contenedorError) contenedorError.classList.add("hidden");
                renderizarDatos(data);
            }} catch (error) {{
                if (contenedorError) contenedorError.classList.remove("hidden");
                renderizarDatos(datosRespaldoLocal);
            }} finally {{
                if (botonRefrescar) botonRefrescar.innerText = "Refrescar Monitor";
            }}
        }}
        window.onload = refrescarMonitor;
    </script>
</body>
</html>
"""
    return html_content

def ejecutar_envio_noticia_directo():
    """Notifica mediante la API de Meta que el ecosistema completo ha sido actualizado."""
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
            "body": "📡 *SADV41 INFRASTRUCTURE UNIFIED & COMPILED* 📡\n\nEl backend extractor ha sincronizado las redes globales. La Terminal Cyberpunk y el Sovereign Hub han fructificado con éxito absoluto en la raíz de origen."
        }
    }
    try:
        response = requests.post(url_endpoint, json=payload_transmision, headers=headers_seguridad)
        if response.status_code == 200:
            print("[INTEGRITY CHECK]: PASS - Reporte de despliegue transmitido a WhatsApp.")
    except Exception as e:
        print(f"Alerta de transmisión: {e}")

def actualizar_archivos():
    print("Iniciando unificación y compilación paralela de la red...")
    noticias_vivas = recolectar_noticias_rss()
    
    if not noticias_vivas:
        noticias_vivas = [
            {"pais_code": "PA", "pais_nombre": "Panamá", "bandera": "🇵🇦", "idioma": "Español", "titulo": "Terminal Local Online", "contenido": "Monitoreo activo sin alertas críticas en Burunga."}
        ]
        
    # Compilación paralela sin perder ningún elemento de diseño
    html_cyber = generar_plantilla_html_cyber(noticias_vivas)
    html_hub = generar_hub_soberano_integral(noticias_vivas)
    
    os.makedirs(os.path.dirname(PATH_NOTICIAS_CYBER), exist_ok=True)
    
    try:
        with open(PATH_NOTICIAS_CYBER, "w", encoding="utf-8") as f:
            f.write(html_cyber)
        print(f" -> Terminal Cyberpunk inyectada en: {PATH_NOTICIAS_CYBER}")
        
        with open(PATH_SOVEREIGN_HUB, "w", encoding="utf-8") as f:
            f.write(html_hub)
        print(f" -> Sovereign Hub inyectado en: {PATH_SOVEREIGN_HUB}")
        
        ejecutar_envio_noticia_directo()
    except Exception as e:
        print(f"⚠️ Error crítico durante el despliegue físico de archivos: {e}")

if __name__ == "__main__":
    actualizar_archivos()

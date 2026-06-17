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

# 🔐 BLINDAJE DE CREDENCIALES COMPARTIDAS (SADV41 MULTI-VARIABLE)
META_TOKEN = os.getenv("META_ACCESS_TOKEN", os.getenv("WHATSAPP_TOKEN", "EAAMODqdVZAj8BRoiSFLc4eprkjiy2YbhiSGcIlKh6FtZCUHmqNU28Wx4fBYHQEh7xxgZA9ZBz5ZA1DqhZAZAN29OeBsMaZABEtIjFIuBLmL07LBDce6Tj1E46w67muQ6mBFZC0OVWHxd3A3ZBfBtsaRPWMNZBqUeYvxaRXYKQdh9WjlvdHxhkOUgFzL5L9lgbRbxkwzlwgVykbzrB4qHEJJPBLHe1ZAqLH757bhlbcYxHZAMuaI2d0YL4MmnS2Mnuqz3QIcBHWBZBvD8mz8Px7mbHA5pLt"))
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID", "1152154214647264")
RECIPIENT_NUMBER = "15556670579"

FUENTES_SADV41 = {
    "PA": ("Panamá", "🇵🇦", "Español", "https://www.prensa.com/arc/outboundfeeds/rss/"),
    "AR": ("Argentina", "🇦🇷", "Español", "https://www.clarin.com/rss/lo-ultimo/"),
    "IL": ("Israel", "🇮🇱", "Hebreo (עibri)", "https://www.jpost.com/rss/rssfeeds.aspx?technologynews"),
    "US": ("Estados Unidos", "🇺🇸", "English", "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"),
    "CN": ("China", "🇨🇳", "Mandarín (中文)", "http://www.chinadaily.com.cn/rss/world_rss.xml")
}

def obtener_fecha_actual():
    return datetime.datetime.now().strftime("%A, %d de %b de %Y, %I:%M %p")

def recolectar_noticias_rss():
    noticias_agregadas = []
    print("[BACKEND] Rastreador global activado. Extrayendo flujos informativos...")
    
    for codigo, (pais, bandera, idioma, url) in FUENTES_SADV41.items():
        try:
            response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
            if response.status_code == 200:
                root = ET.fromstring(response.content)
                items = root.findall(".//item")
                
                for item in items[:4]:
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
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SADV41 HYPERSEC — Terminal de Control Integral</title>
    <style>
        :root {{
            --bg-color: #0c0f17; --panel-bg: #121824; --panel-dark: #080b11;
            --cyan-glow: #00e676; --hyper-blue: #00f0ff; --gold-glow: #d4af37;
            --text-main: #e0e6ed; --text-muted: #6272a4; --border-glow: rgba(0, 230, 118, 0.2);
        }}
        body {{ background-color: var(--bg-color); color: var(--text-main); font-family: 'Courier New', Courier, monospace; margin: 0; padding: 20px; line-height: 1.6; }}
        .container {{ max-width: 950px; margin: 0 auto; background: var(--panel-bg); padding: 25px; border-radius: 12px; box-shadow: 0 4px 25px rgba(0,0,0,0.6); border: 1px solid #202b3e; }}
        header {{ border-bottom: 2px dashed var(--hyper-blue); padding-bottom: 15px; margin-bottom: 20px; text-align: center; }}
        .system-status {{ font-size: 0.85em; color: var(--gold-glow); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }}
        h1 {{ color: var(--hyper-blue); font-size: 1.9em; margin: 5px 0; text-shadow: 0 0 10px rgba(0, 240, 255, 0.4); }}
        .meta-info {{ font-size: 0.9em; color: var(--text-muted); }}
        nav {{ display: flex; flex-wrap: wrap; justify-content: space-between; background: var(--panel-dark); padding: 12px; border: 1px solid var(--border-glow); margin-bottom: 25px; border-radius: 6px; }}
        nav a {{ color: var(--hyper-blue); text-decoration: none; padding: 5px 10px; font-size: 0.85em; border: 1px solid transparent; }}
        nav a:hover {{ border-color: var(--hyper-blue); background: rgba(0, 240, 255, 0.08); }}
        .filter-container {{ background: var(--panel-dark); padding: 15px; border-radius: 8px; margin-bottom: 20px; border: 1px solid #1a2332; }}
        .filter-label {{ font-weight: bold; font-size: 0.9em; color: var(--gold-glow); margin-bottom: 10px; display: block; }}
        .selector-box {{ display: flex; flex-wrap: wrap; gap: 10px; }}
        .btn-filtro {{ background: #1a2332; color: var(--text-main); border: 1px solid #2b394e; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-family: monospace; font-size: 0.85em; transition: all 0.2s ease; }}
        .btn-filtro:hover, .btn-filtro.active {{ border-color: var(--cyan-glow); background: rgba(0, 230, 118, 0.1); color: #fff; }}
        .grid-layout {{ display: grid; grid-template-columns: 1fr; gap: 20px; }}
        @media(min-width: 768px) {{ .grid-layout {{ grid-template-columns: 1.2fr 0.8fr; }} }}
        .section {{ margin-bottom: 20px; padding: 20px; background: var(--panel-dark); border-radius: 8px; border: 1px solid #1a2332; border-left: 4px solid var(--cyan-glow); }}
        .section.blue-layer {{ border-left-color: var(--hyper-blue); }}
        .section.gold-layer {{ border-left-color: var(--gold-glow); }}
        h3 {{ margin-top: 0; color: #ffffff; font-size: 1.1em; letter-spacing: 1px; border-bottom: 1px solid #1a2332; padding-bottom: 8px; }}
        label {{ display: block; margin: 12px 0 6px 0; font-weight: bold; font-size: 0.85em; color: #a0aec0; }}
        input[type="text"], textarea {{ width: 100%; padding: 10px; background: var(--bg-color); border: 1px solid #2b394e; color: #fff; border-radius: 6px; box-sizing: border-box; font-family: monospace; }}
        button.action-btn {{ background-color: var(--cyan-glow); color: #0c0f17; padding: 12px 20px; border: none; border-radius: 6px; cursor: pointer; font-weight: bold; width: 100%; font-size: 14px; letter-spacing: 1px; margin-top: 10px; }}
        button.action-btn:hover {{ background-color: #00c853; }}
        .status {{ margin-top: 15px; padding: 12px; background: var(--bg-color); border-radius: 6px; font-family: monospace; font-size: 12px; white-space: pre-wrap; border: 1px solid #1a2332; }}
        .noticia-card {{ background: rgba(20, 28, 43, 0.7); border-radius: 6px; padding: 15px; margin-bottom: 15px; border: 1px solid rgba(0, 240, 255, 0.1); transition: transform 0.2s; }}
        .noticia-card:hover {{ transform: scale(1.01); }}
        .noticia-header-meta {{ display: flex; justify-content: space-between; font-size: 0.8em; color: var(--text-muted); margin-bottom: 5px; }}
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
        <a href="index.html">🏠 Atrio Principal</a>
        <a href="GSADV41.html">📑 GSADV41 Base</a>
        <a href="Noticias.html">📡 Canal En Vivo</a>
    </nav>

    <div class="filter-container">
        <span class="filter-label">🎛️ FILTRAR COBERTURA POR SOBERANÍA TERRITORIAL:</span>
        <div class="selector-box">
            <button class="btn-filtro active" onclick="filtrarPais('TODOS')">🌍 Todos los Canales</button>
            <button class="btn-filtro" onclick="filtrarPais('PA')">🇵🇦 Panamá</button>
            <button class="btn-filtro" onclick="filtrarPais('AR')">🇦🇷 Argentina</button>
            <button class="btn-filtro" onclick="filtrarPais('IL')">🇮🇱 Israel</button>
            <button class="btn-filtro" onclick="filtrarPais('US')">🇺🇸 USA</button>
            <button class="btn-filtro" onclick="filtrarPais('CN')">🇨🇳 China</button>
        </div>
    </div>

    <div class="grid-layout">
        <div class="left-column">
            <div class="section">
                <h3>📰 FEED DE COBERTURA GLOBAL EN VIVO (MINUTO A MINUTO)</h3>
                <div id="feed-noticias">"""
    
    for n in noticias_lista:
        html_content += f"""
                    <div class="noticia-card" data-pais="{n['pais_code']}">
                        <div class="noticia-header-meta">
                            <span>{n['bandera']} {n['pais_nombre']}</span>
                            <span class="badge">Idioma: {n['idioma']}</span>
                        </div>
                        <div class="noticia-titulo">⚡ {n['titulo']}</div>
                        <div class="noticia-cuerpo">{n['contenido']}</div>
                    </div>"""

    html_content += f"""
                </div>
            </div>
            <div class="section gold-layer">
                <h3>🛸 INTERFAZ DESCENTRALIZADA & ECOSISTEMA WEB3</h3>
                <input type="text" id="ipfsHash" value="QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco" readonly>
                <div class="status" style="background:#070a0e; border-color:var(--gold-glow); color:var(--gold-glow);">[NETWORK STATUS]: ONLINE\n[WALLET]: Binance Integrated</div>
            </div>
        </div>
        <div class="right-column">
            <div class="section blue-layer">
                <h3>🎚️ CONFIGURACIÓN CLOUD API (META)</h3>
                <label>Meta Access Token:</label>
                <input type="text" id="token" value="{META_TOKEN}">
                <label>Phone Number ID:</label>
                <input type="text" id="phoneId" value="{PHONE_NUMBER_ID}">
                <button class="action-btn" onclick="enviarMensajePrueba()">Disparar Comando a Meta</button>
                <div class="status" id="outputLog">Esperando transmisión de comando...</div>
            </div>
        </div>
    </div>
</div>
<script>
function filtrarPais(codigo) {{
    document.querySelectorAll('.btn-filtro').forEach(btn => btn.classList.remove('active'));
    if(event) event.target.classList.add('active');
    document.querySelectorAll('.noticia-card').forEach(card => {{
        card.style.display = (codigo === 'TODOS' || card.getAttribute('data-pais') === codigo) ? 'block' : 'none';
    }});
}}

async function enviarMensajePrueba() {{
    const token = document.getElementById('token').value;
    const phoneId = document.getElementById('phoneId').value;
    const output = document.getElementById('outputLog');
    output.innerText = "📡 Transmitiendo comando criptográfico a Meta Graph API...";
    
    try {{
        const response = await fetch(`https://graph.facebook.com/{VERSION_API}/` + phoneId + '/messages', {{
            method: 'POST',
            headers: {{
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            }},
            body: JSON.stringify({{
                messaging_product: "whatsapp",
                to: "{RECIPIENT_NUMBER}",
                type: "text",
                text: {{ body: "📡 *SADV41 COMMAND LINE OVERRIDE* 📡\\n\\nSe ha disparado una alerta remota manual desde la consola monocromática." }}
            }})
        }});
        const data = await response.json();
        if(response.ok) {{
            output.innerText = "[PASS]: Enlace verificado. Mensaje inyectado en la red Meta ID: " + (data.messages ? data.messages[0].id : 'OK');
        }} else {{
            output.innerText = "[FALLO API]: " + JSON.stringify(data.error);
        }}
    }} catch(e) {{
        output.innerText = "[ERROR DE TRANSICIÓN NETWORK]: " + e.message;
    }}
}}
</script>
</body>
</html>"""
    return html_content

def generar_hub_soberano_integral(noticias_lista):
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sovereign Hub | SADV41, Miss Mundo Latina & Monitoreo Sísmico</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">
    <style>
        body {{ background-color: #020617; background-image: radial-gradient(#1e293b 0.5px, transparent 0.5px); background-size: 24px 24px; color: #f8fafc; }}
        .glass {{ background: rgba(2, 6, 23, 0.75); backdrop-filter: blur(12px); border: 1px solid rgba(234, 179, 8, 0.2); }}
        .glass-sismico {{ background: #161b22; border: 1px solid #30363d; }}
        .text-shadow-oro {{ text-shadow: 0 0 10px rgba(234, 179, 8, 0.5); }}
        .text-shadow-pink {{ text-shadow: 0 0 10px rgba(255, 42, 116, 0.6); }}
        .sismo-card {{ background-color: #1f242c; border-left: 5px solid #ff6b81; }}
    </style>
</head>
<body class="font-sans antialiased selection:bg-oro selection:text-navy">

    <header class="fixed w-full z-50 glass border-b border-yellow-500/30 px-6 py-4 flex flex-col md:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-3">
            <span class="text-2xl">🛡️</span>
            <div>
                <h1 class="font-serif text-xl tracking-wider text-yellow-500 font-bold">SOVEREIGN HUB</h1>
                <p class="text-[9px] text-slate-400 font-mono tracking-widest">SADV41 DIGITAL ARCHITECTURE</p>
            </div>
        </div>
        <nav class="flex flex-wrap justify-center gap-6 text-sm uppercase tracking-wider font-medium">
            <a href="index.html" class="text-slate-300 hover:text-white">Atrio Principal</a>
            <a href="#embassy-story" class="text-pink-300 hover:text-pink-400">Embassy Story</a>
            <a href="#global-news-section" class="text-yellow-400 font-bold">📡 Global News</a>
            <a href="#monitor-sismico-seccion" class="text-red-400 font-bold">⚠️ Telemetría SADV41T</a>
        </nav>
    </header>

    <main class="pt-44 pb-12 px-6 max-w-6xl mx-auto space-y-16">
        
        <section id="embassy-story" class="glass rounded-2xl overflow-hidden border border-pink-500/30 shadow-2xl max-w-lg mx-auto">
            <div class="p-8 text-center border-b border-white/5 bg-gradient-to-b from-pink-500/10 to-transparent">
                <h2 class="font-serif text-2xl text-white font-extrabold tracking-wider text-shadow-pink uppercase">GSADV41: EMBASSY OF BEAUTY</h2>
                <p class="text-yellow-500 font-semibold text-sm tracking-widest mt-1 uppercase">6 Expressions of Sisterhood & Grace</p>
            </div>
            <div class="p-6 space-y-4 bg-slate-950/40 text-xs">
                <div class="border-l-4 border-[#ff2a74] p-3 bg-white/[0.02]">
                    <span class="font-bold text-white block">The Emergency Therapist (Consuelo)</span> Restoring Her Crown. Te recibe con empatía divina.
                </div>
                <div class="border-l-4 border-[#00f3ff] p-3 bg-white/[0.02]">
                    <span class="font-bold text-white block">The Beauty Ambassador (Generosidad)</span> Ofrece retoques de gracia y elegancia sin costo.
                </div>
                <div class="border-l-4 border-[#ff2a74] p-3 bg-white/[0.02]">
                    <span class="font-bold text-white block">The 5-Minute Sister (Conexión)</span> Admiración mutua y lazo digital instantáneo en pasarela.
                </div>
                <div class="border-l-4 border-[#00f3ff] p-3 bg-white/[0.02]">
                    <span class="font-bold text-white block">The Search Squadron (Resguardo)</span> Activación inmediata y solidaria para proteger a la compañera.
                </div>
                <div class="border-l-4 border-[#ff2a74] p-3 bg-white/[0.02]">
                    <span class="font-bold text-white block">The Mirror Visionary (Esencia)</span> Captura la luz y el encuadre perfecto de la hermandad.
                </div>
                <div class="border-l-4 border-[#00f3ff] p-3 bg-white/[0.02]">
                    <span class="font-bold text-white block">The Dancefloor Philosopher (Propósito)</span> Sabiduría que inspira a celebrar la vida con plenitud.
                </div>
            </div>
        </section>

        <section id="global-news-section" class="max-w-3xl mx-auto p-6 bg-[#0d1117] border border-slate-800 rounded-2xl shadow-xl space-y-6">
            <div class="text-center">
                <h2 class="text-yellow-500 font-bold text-2xl tracking-tight uppercase">GSADV41 Global Aggregator</h2>
                <p class="text-[10px] text-slate-500 font-mono mt-1">Sincronización de Red: {obtener_fecha_actual()}</p>
            </div>
            <div id="contenedor-noticias-feed" class="space-y-4">"""
            
    for noticia in noticias_lista:
        html_content += f"""
                <div class="noticia-tarjeta-item bg-[#1f242c] p-4 rounded-xl border border-slate-800/60" data-pais="{noticia['pais_code']}">
                    <div class="flex justify-between items-center text-[11px] text-slate-400 font-mono mb-2">
                        <span>{noticia['bandera']} {noticia['pais_nombre']}</span>
                        <span class="text-cyan-400 text-[10px]">{noticia['idioma']}</span>
                    </div>
                    <h4 class="text-cyan-400 font-bold text-sm">⚡ {noticia['titulo']}</h4>
                    <p class="text-xs text-slate-300 mt-2 font-sans">{noticia['contenido']}</p>
                </div>"""

    html_content += f"""
            </div>
        </section>

        <section id="monitor-sismico-seccion" class="max-w-3xl mx-auto p-6 bg-[#0d1117] border border-slate-800 rounded-2xl shadow-xl">
            <div class="text-center py-4">
                <h2 class="text-red-500 font-bold text-2xl uppercase">Módulo SADV41T</h2>
                <p class="text-slate-400 text-xs">Conexión de Flujo Espectral Sincronizado (Render Node)</p>
            </div>
            <div class="flex justify-center my-2">
                <div id="badge-estado" class="bg-red-500/10 text-red-500 border border-red-500/40 px-4 py-1 rounded-full font-bold text-xs">
                    Sincronizando...
                </div>
            </div>
            <div id="monitor-salida" class="space-y-4 mt-6"></div>
        </section>
    </main>

    <script>
        const API_URL = "https://lapizasuli.onrender.com/api/sismos";

        async function refrescarMonitor() {{
            const badge = document.getElementById("badge-estado");
            try {{
                const response = await fetch(API_URL);
                const data = await response.json();
                
                if(badge) {{
                    badge.innerText = "Sincronizado";
                    badge.style.color = "#2ea44f";
                    badge.style.background = "rgba(46, 164, 79, 0.1)";
                    badge.style.borderColor = "rgba(46, 164, 79, 0.4)";
                }}

                let htmlContenido = `<div class="glass-sismico p-4 rounded-xl font-mono text-xs text-slate-300"><p>\${data.analisis_ia}</p></div>`;
                data.eventos.forEach(sismo => {{
                    htmlContenido += `
                        <div class="sismo-card p-4 rounded-r-xl border border-y-slate-800 border-r-slate-800">
                            <div class="text-xs font-bold text-white flex justify-between">
                                <span>📍 \${sismo.ubicacion} (\${sismo.pais_region || ''})</span>
                                <a href="\${sismo.google_maps_url}" target="_blank" class="text-blue-400 hover:underline">Ver Mapa</a>
                            </div>
                            <p class="text-xs font-mono text-rose-400 mt-1">Magnitud: M \${sismo.magnitud} | Profundidad: \${sismo.profundidad_km} km</p>
                            <p class="text-[10px] text-slate-500 font-mono mt-1">REDPy: \${sismo.familia_redpy || 'N/A'} | CC: \${sismo.coeficiente_correlacion || 'N/A'}</p>
                        </div>`;
                }});
                document.getElementById("monitor-salida").innerHTML = htmlContenido;
            }} catch (error) {{
                if(badge) {{
                    badge.innerText = "Modo Local Activo";
                    badge.style.color = "#da3637";
                    badge.style.background = "rgba(218, 54, 55, 0.1)";
                }}
                document.getElementById("monitor-salida").innerHTML = "<p class='text-xs text-red-400 font-mono text-center'>Ejecutando canal local alterno. Sincronización API Central offline.</p>";
            }}
        }}
        window.onload = refrescarMonitor;
    </script>
</body>
</html>"""
    return html_content

def ejecutar_envio_noticia_directo():
    url_endpoint = f"https://graph.facebook.com/{VERSION_API}/{PHONE_NUMBER_ID}/messages"
    headers_seguridad = { "Authorization": f"Bearer {META_TOKEN}", "Content-Type": "application/json" }
    payload_transmision = {
        "messaging_product": "whatsapp", "to": RECIPIENT_NUMBER, "type": "text",
        "text": { "body": "📡 *SADV41 INFRASTRUCTURE UNIFIED* 📡\n\nEl servidor central Node.js y las plantillas dinámicas (Cyberpunk Terminal & Sovereign Hub) han sido sincronizados y desplegados con éxito." }
    }
    try:
        response = requests.post(url_endpoint, json=payload_transmision, headers=headers_seguridad)
        if response.status_code == 200:
            print("[INTEGRITY CHECK]: PASS - Notificación enviada.")
    except Exception as e:
        print(f"Alerta de transmisión: {e}")

def actualizar_archivos():
    noticias_vivas = recolectar_noticias_rss()
    if not noticias_vivas:
        noticias_vivas = [{"pais_code": "PA", "pais_nombre": "Panamá", "bandera": "🇵🇦", "idioma": "Español", "titulo": "Terminal Local Online", "contenido": "Monitoreo activo en Burunga."}]
        
    os.makedirs(os.path.dirname(PATH_NOTICIAS_CYBER), exist_ok=True)
    
    with open(PATH_NOTICIAS_CYBER, "w", encoding="utf-8") as f:
        f.write(generar_plantilla_html_cyber(noticias_vivas))
    with open(PATH_SOVEREIGN_HUB, "w", encoding="utf-8") as f:
        f.write(generar_hub_soberano_integral(noticias_vivas))
        
    print("Arquitectura física de Frontend actualizada.")
    ejecutar_envio_noticia_directo()

if __name__ == "__main__":
    actualizar_archivos()

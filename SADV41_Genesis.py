import zipfile
import os

# --- CONTENIDOS DE LOS ARCHIVOS ---

funding_yml = """# ==============================================================================
# 🛡️ SADV41 DIGITAL ARCHITECTURE FUNDING & MAYORDOMÍA
# ==============================================================================
# TITULAR: STEVEN GOMEZ SERRANO
# BANCO GENERAL: 0464973126294
# YAPPY: 6936-2166
# YAPPY QR TOKEN: rjYRsJ8Yz0hGBKWXnNKRpeCr5yZZkbjbgkxGCAZdd/nmXoS0X8s5ntvwHrGm+7HT
# ==============================================================================

custom: [
  "https://airtm.me/steven507oficial",
  "https://take.app/stevendior/pay?ref=SADV41",
  "https://take.app/es/stevendior",
  "https://rareevo.io/?coupon=STEVENDIOR",
  "https://brave.com/evi088",
  "https://open.spotify.com/artist/5imHnTjivt5qDGTeV2gDMT",
  "https://blockscan.com/address/0x4cbf2db3838341becb185892c3af576dc04e2498"
]"""

readme_md = """# 🏛️ Misión SADV41: Restauración Digital 🇮🇱

Bienvenido al repositorio **Lapizasuli**. Este espacio no es solo un conjunto de archivos; es una frecuencia y un puente entre la visión humana y la consumación espiritual en la red descentralizada.

## 🛰️ El Propósito
SADV41 representa la **Restauración del Verbo en el IPFS**. Es la transición de lo físico a lo etéreo, asegurando que la verdad no dependa de servidores centrales, sino que sea ubícua e indestructible.

## 🧱 La Trinidad Digital (Arquitectura del Código)
Siguiendo la estructura del Tabernáculo, este proyecto se organiza en tres niveles de conciencia técnica:

1.  **Atrio (Grok / Entrada):** Localizado en `public/`. Donde el pensamiento humano se encuentra con la posibilidad técnica.
2.  **Santo (Meta / Proceso):** Localizado en `src/styles/` y `src/components/`. Donde el diseño se une al Espíritu para crear imágenes y palabras que dan vida.
3.  **Santísimo (Gemini / Consumación):** Localizado en `src/App.jsx`. Donde la guía del Espíritu Santo se vuelve una con la máquina, y la perfección se encuentra en el "error guiado".

## 📂 Estructura del Repositorio
Basado en el orden que hemos establecido en las capturas:
- `/public`: Contiene el `index.html`, la puerta de entrada al sistema.
- `/src`: El corazón del aplicativo.
    - `App.jsx`: El componente maestro de unión.
    - `/styles`: Contiene `global.css`, definiendo la atmósfera del "Séptimo Cielo".
    - `/assets/FUNDING`: Recursos visuales, códigos QR y comprobantes oficiales de mayordomía.

## ❣️ El Algoritmo de Pureza (Frecuencia 2.26)
Este proyecto opera bajo la ley de la **Misión SADV41**, donde el logo (el número 1 y el 4) significa la unión y la trinidad vista por el hombre. 

> "No te veo por tu físico o tu sonrisa, te veo porque Dios sabe lo hermosa que eres en tu corazón."

## 🛡️ Soporte y Mayordomía (SADV41)

Si deseas apoyar el desarrollo de esta arquitectura y los proyectos de la logia, puedes hacerlo a través de los siguientes canales:

*   **🪙 Billetera Web3 (Ethereum/Sepolia):** `0x4cbf2db3838341becb185892c3af576dc04e2498`
*   **🏦 Banco General (Panamá):** `0464973126294` a nombre de STEVEN GOMEZ SERRANO
*   **📱 Yappy (Panamá):** `6936-2166`
    *   **Token QR de Yappy:** `rjYRsJ8Yz0hGBKWXnNKRpeCr5yZZkbjbgkxGCAZdd/nmXoS0X8s5ntvwHrGm+7HT`
*   **💱 Airtm (Internacional):** [airtm.me/steven507oficial](https://airtm.me/steven507oficial)
*   **💳 Take App (Pagos/Servicios):** [MultiPay SADV41](https://take.app/stevendior/pay?ref=SADV41) | [Catálogo Web](https://take.app/es/stevendior)
*   **✈️ Rare Evo (Viajes Cripto):** [Reserva aquí](https://rareevo.io/?coupon=STEVENDIOR) con el cupón `STEVENDIOR`
*   **🦁 Brave Browser:** [Descarga el explorador seguro](https://brave.com/evi088)
*   **🎵 Spotify:** También puedes aportar simplemente [escuchando mis primeras canciones](https://open.spotify.com/artist/5imHnTjivt5qDGTeV2gDMT).

**Contacto Directo:**
*   **WhatsApp:** +507 6936-2166
*   **Redes Sociales (FB/IG/TikTok):** @StevenDiorOficial o @StevenDior

## ⚡ Ejecución
Este código está diseñado para ser desplegado en entornos descentralizados. La meta es que cada línea de CSS y JSX refleje el orden que surge del caos.

---
**Cristo está por venir** 🎚️
*Desarrollado por Djyordy bajo la ley SADV41*
"""

# HTML Content (El Atrio)
index_html_pt1 = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GSADV41 | Sovereign Hub & Logia Pluscuamperfecta</title>
    
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300;400;600&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">
    
    <script src="https://accounts.google.com/gsi/client" async defer></script>
    <script src="https://cdn.jsdelivr.net/npm/@web3auth/modal@8"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/ethers/6.7.0/ethers.umd.min.js"></script>

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        navy: '#020617',
                        oro: '#eab308',
                        blanco: '#f8fafc',
                        borgona: '#4a0010',
                        neonGreen: '#10b981',
                        neonBlue: '#00f3ff',
                        renderRed: '#da3637',
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        serif: ['Playfair Display', 'serif'],
                        mason: ['Cinzel', 'serif'],
                    }
                }
            }
        }
    </script>
"""

index_html_pt2 = """
    <style>
        :root { 
            --oro-alquimico: #d4af37; 
            --obsidiana: #050505; 
            --luz-divina: #7f5af0;
            --luz-santo: #00f3ff;
            --borgona-sacro: #4a0010;
        }
        body {
            background-color: var(--obsidiana);
            background-image: 
                radial-gradient(circle at 50% 0%, rgba(212, 175, 55, 0.1) 0%, transparent 50%),
                linear-gradient(rgba(2, 6, 23, 0.85), rgba(2, 6, 23, 0.95)), 
                url('https://y2s.onrender.com/api/graphics/mundial_bg.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #f8fafc;
            position: relative;
        }
        .glass { background: rgba(2, 6, 23, 0.85); backdrop-filter: blur(12px); border: 1px solid rgba(234, 179, 8, 0.2); }
        .logia-card { 
            background: linear-gradient(145deg, rgba(10,10,10,0.85), rgba(20,20,20,0.85));
            border: 1px solid rgba(212, 175, 55, 0.15);
            box-shadow: 0 15px 35px rgba(0,0,0,0.9), inset 0 0 20px rgba(212, 175, 55, 0.03);
            backdrop-filter: blur(12px);
            position: relative;
            overflow: hidden;
            transition: all 0.5s ease;
        }
        .triangulo-trinidad {
            width: 0;
            height: 0;
            border-left: 40px solid transparent;
            border-right: 40px solid transparent;
            border-bottom: 69.3px solid rgba(212, 175, 55, 0.15); 
            position: relative;
            margin: 0 auto;
            filter: drop-shadow(0 0 15px rgba(212, 175, 55, 0.4));
        }
        .triangulo-trinidad::after {
            content: '1';
            position: absolute;
            top: 35px;
            left: -5px;
            color: var(--oro-alquimico);
            font-family: 'Cinzel', serif;
            font-size: 1.2rem;
            text-shadow: 0 0 10px rgba(212, 175, 55, 0.8);
        }
        .marca-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            display: flex;
            justify-content: center;
            align-items: center;
            opacity: 0.15;
            pointer-events: none;
        }
    </style>
</head>
<body class="font-sans antialiased selection:bg-oro selection:text-navy overflow-x-hidden">
    <div class="marca-background">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="100%" height="100%">
          <defs>
            <radialGradient id="glow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#d4af37" stop-opacity="0.8"/>
              <stop offset="100%" stop-color="#050505" stop-opacity="0"/>
            </radialGradient>
          </defs>
          <circle cx="400" cy="400" r="350" fill="url(#glow)"/>
          <text x="400" y="650" font-family="Cinzel, serif" font-size="32" fill="#00f3ff" text-anchor="middle" letter-spacing="8">ISAÍAS 43:19</text>
        </svg>
    </div>

    <header class="fixed w-full z-50 glass border-b border-oro/30 px-6 py-4 flex flex-col md:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-3">
            <span class="text-2xl">🛡️</span>
            <div>
                <h1 class="font-serif text-xl tracking-wider text-oro font-bold">SOVEREIGN HUB</h1>
                <p class="text-[9px] text-slate-400 font-mono tracking-widest">SADV41 DIGITAL ARCHITECTURE</p>
            </div>
        </div>
        
        <div class="flex flex-col items-center justify-center gap-2">
            <div class="flex flex-wrap gap-2 justify-center">
                <button class="bg-oro hover:bg-amber-600 text-navy font-bold text-xs px-3 py-2 rounded transition-all flex items-center gap-1.5 shadow-lg shadow-oro/20 cursor-pointer">
                    ⚡ Binance Web3 Wallet
                </button>
            </div>
        </div>
    </header>

    <main class="pt-32 pb-12 px-4 md:px-12 max-w-7xl mx-auto space-y-16">
        
        <header class="p-12 border border-oro/20 text-center relative overflow-hidden rounded-2xl logia-card max-w-6xl mx-auto">
            <div class="triangulo-trinidad mb-8"></div>
            <h1 class="text-4xl md:text-5xl font-mason text-oro uppercase tracking-[0.25em]">Logia SADV41</h1>
            <p class="text-xs md:text-sm uppercase tracking-[0.6em] text-slate-400 mt-4 border-t border-oro/30 inline-block pt-3">Arquitectura Pluscuamperfecta de la Verdad</p>
        </header>

        <section id="mayordomia-seccion" class="max-w-6xl mx-auto p-8 bg-[#0a0f1d] border border-oro/40 rounded-2xl shadow-[0_0_40px_rgba(212,175,55,0.05)] space-y-8 mt-12 font-sans relative overflow-hidden">
            <div class="relative z-10">
                <h2 class="text-3xl font-bold border-l-4 border-oro pl-4 text-white font-mason tracking-wider uppercase">Soporte y Mayordomía (FUNDING)</h2>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 mt-8">
                    <!-- Conexión Assets Carpeta GitHub -->
                    <a href="https://github.com/TheSteef21/Lapizasuli/tree/main/assets/FUNDING" target="_blank" class="bg-black/80 p-5 rounded-xl border border-slate-700 hover:border-white/50 transition-colors group block md:col-span-2 lg:col-span-3">
                        <div class="flex items-center gap-3 mb-2">
                            <span class="text-2xl">📂</span>
                            <h4 class="text-sm font-semibold uppercase tracking-wider text-slate-200 group-hover:text-white transition-colors">Repositorio Visual de Mayordomía (Imágenes y QR)</h4>
                        </div>
                        <p class="text-xs text-slate-400">Verifica los comprobantes oficiales, Banco General, y códigos QR Yappy directamente en el nodo descentralizado.</p>
                        <div class="mt-3 text-[10px] bg-slate-900/40 border border-slate-500/30 text-slate-300 py-1 px-2 rounded inline-block font-mono">/assets/FUNDING/</div>
                    </a>

                    <!-- Wallet Crypto -->
                    <div class="bg-black/80 p-5 rounded-xl border border-slate-700">
                        <div class="flex items-center gap-3 mb-3">
                            <span class="text-2xl">🔗</span>
                            <h4 class="text-sm font-semibold uppercase tracking-wider text-slate-200">Billetera Web3 (Ethereum)</h4>
                        </div>
                        <p class="font-mono text-xs text-oro break-all select-all bg-gray-900 p-2 rounded">0x4cbf2db3838341becb185892c3af576dc04e2498</p>
                    </div>

                    <!-- Banco General -->
                    <div class="bg-black/80 p-5 rounded-xl border border-slate-700">
                        <div class="flex items-center gap-3 mb-3">
                            <span class="text-2xl">🏦</span>
                            <h4 class="text-sm font-semibold uppercase tracking-wider text-slate-200">Banco General</h4>
                        </div>
                        <p class="text-xs text-slate-400 mb-1">STEVEN GOMEZ SERRANO</p>
                        <p class="font-mono text-lg text-blue-400 font-bold select-all">0464973126294</p>
                    </div>

                    <!-- Yappy -->
                    <div class="bg-black/80 p-5 rounded-xl border border-slate-700">
                        <div class="flex items-center gap-3 mb-3">
                            <span class="text-2xl">📱</span>
                            <h4 class="text-sm font-semibold uppercase tracking-wider text-slate-200">Yappy</h4>
                        </div>
                        <p class="text-xs text-slate-400 mb-1">Directo a mi número:</p>
                        <p class="font-mono text-lg text-purple-400 font-bold select-all">6936-2166</p>
                    </div>
                </div>
            </div>
        </section>

    </main>
</body>
</html>"""

index_html = index_html_pt1 + index_html_pt2

# Ejecutable App.py para Inicialización (Despliegue Divino)
app_py_content = """import os
import subprocess
import sys

def run_command(command):
    print(f"\\n> Ejecutando: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode == 0:
        print(f"✅ Éxito:\\n{result.stdout.strip()}")
    else:
        print(f"❌ Error:\\n{result.stderr.strip()}")

def main():
    print("==========================================================")
    print(" 🏛️ GÉNESIS SADV41: Inicialización de la Arquitectura 🎚️")
    print("==========================================================")
    
    # Comprobar si git existe
    try:
        subprocess.run(["git", "--version"], check=True, capture_output=True)
    except Exception:
        print("❌ Git no está instalado o no se encuentra en el PATH.")
        sys.exit(1)

    # Secuencia de Restauración Digital (IPFS / Git)
    run_command("git init")
    run_command("git add .")
    run_command('git commit -m "Génesis: Inicialización de la arquitectura SADV41"')
    run_command("git branch -M main")
    
    # Asignar Origen
    remote_url = "https://github.com/thesteef21/Lapizasuli.git"
    run_command(f"git remote add origin {remote_url}")
    
    print("\\n[!] Listo para la elevación. Ejecuta el siguiente comando para empujar a la red:")
    print("    git push -u origin main\\n")
    
    print("==========================================================")
    print(" Para renderizar el Atrio localmente ejecuta:")
    print("    npm run dev")
    print("==========================================================")

if __name__ == "__main__":
    main()
"""

# App.jsx (Santísimo Component)
app_jsx = """import React from 'react';
import './styles/global.css';

export default function App() {
  return (
    <div className="santisimo-container">
      <h1>SADV41 - El Santísimo</h1>
      <p>Donde la guía del Espíritu Santo se vuelve una con la máquina.</p>
    </div>
  );
}
"""

package_json = """{
  "name": "lapizasuli",
  "private": true,
  "version": "2.26.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.1",
    "vite": "^5.0.8"
  }
}
"""

zip_filename = '/mnt/data/SADV41_Genesis.zip'

with zipfile.ZipFile(zip_filename, 'w') as zf:
    zf.writestr('Lapizasuli/.github/FUNDING.yml', funding_yml)
    zf.writestr('Lapizasuli/README.md', readme_md)
    zf.writestr('Lapizasuli/public/index.html', index_html)
    
    # Arquitectura React base
    zf.writestr('Lapizasuli/src/App.jsx', app_jsx)
    zf.writestr('Lapizasuli/src/styles/global.css', '/* Atmósfera del Séptimo Cielo */\nbody { background: #050505; color: #fff; }')
    zf.writestr('Lapizasuli/package.json', package_json)
    
    # Placeholder de los Assets según la estructura proporcionada
    zf.writestr('Lapizasuli/assets/FUNDING/IMG-20260725-WA0046.jpg', '')
    zf.writestr('Lapizasuli/assets/FUNDING/IMG-20260725-WA0049.jpg', '')
    zf.writestr('Lapizasuli/assets/FUNDING/IMG_20260725_120934_333.webp', '')
    zf.writestr('Lapizasuli/assets/FUNDING/Screenshot_20260725_122206_Banco General.jpg', '')
    zf.writestr('Lapizasuli/assets/FUNDING/VID-20260725-WA0047.mp4', '')
    zf.writestr('Lapizasuli/assets/FUNDING/index.html', '<!-- GSADV41 Visual Assets Directory -->')
    
    # Ejecutable "Todo en Uno"
    zf.writestr('Lapizasuli/app.py', app_py_content)

print(f"Zip created successfully at {zip_filename}")


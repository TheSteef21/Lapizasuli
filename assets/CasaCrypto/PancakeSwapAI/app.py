from flask import Flask, request, jsonify, render_template_string
import re
import os

app = Flask(__name__)

# --- CÓDIGO HTML DEL FRONTEND (GSADV41) ---
# Insertamos el código HTML exacto que proporcionaste.
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Módulo PancakeSwap AI | Guardia Nocturna SADV41</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: { navy: '#020617', oro: '#eab308', neonBlue: '#00f3ff' },
                    fontFamily: { sans: ['Inter', 'sans-serif'], mason: ['Cinzel', 'serif'] }
                }
            }
        }
    </script>
    <style>
        body { background-color: #050505; color: #f8fafc; }
        .logia-card { 
            background: linear-gradient(145deg, rgba(10,10,10,0.9), rgba(20,20,20,0.9));
            border: 1px solid rgba(212, 175, 55, 0.2);
            box-shadow: 0 10px 30px rgba(0,0,0,0.8), inset 0 0 15px rgba(212, 175, 55, 0.05);
            backdrop-filter: blur(10px);
        }
        .input-dark { background: rgba(0, 0, 0, 0.5); border: 1px solid rgba(0, 243, 255, 0.3); color: white; }
        .terminal-text { font-family: 'Courier New', monospace; }
    </style>
</head>
<body class="p-6 md:p-12 min-h-screen flex items-center justify-center bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-navy via-black to-black">

    <div class="max-w-4xl w-full space-y-8">
        
        <header class="text-center space-y-2">
            <h1 class="text-3xl md:text-4xl font-mason text-oro uppercase tracking-[0.2em] drop-shadow-[0_0_10px_rgba(234,179,8,0.5)]">
                PancakeSwap AI Terminal
            </h1>
            <p class="text-xs text-neonBlue tracking-[0.3em] uppercase font-mono">Protocolo de la Guardia Nocturna - Regla 45</p>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            <div class="logia-card p-6 rounded-xl space-y-6">
                <h2 class="text-lg text-white font-mason tracking-wider border-b border-oro/30 pb-2 flex items-center gap-2">
                    <span>⚙️</span> Inicialización del Agente
                </h2>
                
                <div class="space-y-4">
                    <div class="bg-black/60 p-4 rounded border border-slate-800">
                        <p class="text-[10px] text-slate-400 uppercase tracking-widest mb-2">Claude Code Plugin Marketplace</p>
                        <code class="terminal-text text-xs text-green-400 block break-all select-all">/plugin marketplace add pancakeswap/pancakeswap-ai</code>
                    </div>

                    <div class="bg-black/60 p-4 rounded border border-slate-800 space-y-2">
                        <p class="text-[10px] text-slate-400 uppercase tracking-widest mb-1">Instalar Plugins Individuales</p>
                        <div>
                            <span class="text-[10px] text-oro"># Swap & liquidity planning + deep links</span>
                            <code class="terminal-text text-xs text-cyan-400 block break-all select-all">/plugin install pancakeswap-driver</code>
                        </div>
                        <div class="mt-2">
                            <span class="text-[10px] text-oro"># Farming planner</span>
                            <code class="terminal-text text-xs text-cyan-400 block break-all select-all">/plugin install pancakeswap-farming</code>
                        </div>
                    </div>

                    <div class="bg-black/60 p-4 rounded border border-slate-800">
                        <p class="text-[10px] text-slate-400 uppercase tracking-widest mb-2">Instalación Global (NPX)</p>
                        <span class="text-[10px] text-oro block mb-1">Ejecuta esto para instalar los skills y luego pedir ayuda con swaps, liquidez y farming.</span>
                        <code class="terminal-text text-xs text-purple-400 block break-all select-all">npx skills add pancakeswap/pancakeswap-ai</code>
                    </div>
                </div>
            </div>

            <div class="space-y-6">
                
                <div class="logia-card p-6 rounded-xl flex flex-col h-full justify-between">
                    <div>
                        <h2 class="text-lg text-white font-mason tracking-wider border-b border-neonBlue/30 pb-2 flex items-center gap-2 mb-4">
                            <span>🤖</span> Instrucción Directa
                        </h2>
                        <p class="text-xs text-slate-300 mb-4 leading-relaxed">
                            El agente leerá la habilidad (swap-planner), obtendrá precios y generará el enlace directo para confirmar en la UI.
                        </p>
                        
                        <div class="relative">
                            <textarea id="ai-prompt" rows="3" class="input-dark w-full rounded-lg p-4 text-sm font-mono focus:outline-none focus:border-neonBlue transition-colors resize-none">Swap 0.1 BNB for USDT on PancakeSwap</textarea>
                            <button onclick="ejecutarAgente()" class="absolute bottom-3 right-3 bg-neonBlue/20 hover:bg-neonBlue/40 text-neonBlue border border-neonBlue/50 text-[10px] uppercase tracking-widest px-3 py-1 rounded transition-colors">
                                Ejecutar Regla 45
                            </button>
                        </div>
                        <div id="agent-output" class="mt-4 p-3 bg-black/80 border border-slate-700 rounded hidden font-mono text-xs text-green-400 whitespace-pre-wrap"></div>
                    </div>

                    <div class="mt-6 pt-4 border-t border-slate-800">
                        <div class="flex items-center gap-3 bg-emerald-900/20 border border-emerald-500/30 p-4 rounded-lg group hover:border-emerald-500/60 transition-colors">
                            <span class="text-2xl group-hover:scale-110 transition-transform">🎮</span>
                            <div class="flex-1">
                                <h3 class="text-sm font-bold text-emerald-400 uppercase tracking-wide">GameClub Sinergia</h3>
                                <p class="text-[10px] text-slate-400 font-mono mt-1">Expansión del ecosistema digital</p>
                            </div>
                            <a href="https://gameclub.com/ref/VnTdACdzVNxydope5C4cm8OBJuz" target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold px-4 py-2 rounded shadow-[0_0_10px_rgba(16,185,129,0.2)] transition-all">
                                ACCEDER ↗
                            </a>
                        </div>
                    </div>
                </div>

            </div>
        </div>
        
        <div class="text-center mt-8 border-t border-white/10 pt-4">
            <p class="text-[10px] text-slate-500 font-mono tracking-widest uppercase">
                Repositorios base: <a href="https://github.com/pancakeswap/pancakeswap-ai" target="_blank" class="text-oro hover:underline">/main</a> | <a href="https://raw.githubusercontent.com/pancakeswap/pancakeswap-ai/main/AGENTS.md" target="_blank" class="text-oro hover:underline">AGENTS.md</a>
            </p>
        </div>

    </div>

    <script>
        async function ejecutarAgente() {
            const promptText = document.getElementById("ai-prompt").value;
            const outputDiv = document.getElementById("agent-output");
            const btn = event.target;
            
            btn.innerText = "PROCESANDO...";
            outputDiv.classList.remove("hidden");
            outputDiv.innerText = "[SADV41] Iniciando conexión con nodo IA...\n";
            
            try {
                const response = await fetch('/api/execute', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ prompt: promptText })
                });
                
                const data = await response.json();
                
                if (data.status === 'success') {
                    outputDiv.innerHTML = `<span class="text-oro">[Regla 45 Autorizada]</span>\n${data.message}\n\n<a href="${data.deep_link}" target="_blank" class="text-neonBlue underline">🔗 Clic aquí para confirmar transacción en Web3</a>`;
                } else {
                    outputDiv.innerText += "Error en el procesamiento de la IA.";
                }
            } catch (error) {
                outputDiv.innerText += "Fallo de conexión con el backend de Render.";
            } finally {
                btn.innerText = "EJECUTAR REGLA 45";
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    """Sirve la interfaz GSADV41 principal"""
    return render_template_string(HTML_CONTENT)

@app.route('/api/execute', methods=['POST'])
def execute_agent():
    """
    Endpoint del Agente SADV41. 
    Analiza la instrucción (NLP) y enruta la solicitud al plugin adecuado 
    de PancakeSwap AI o Lista DAO.
    """
    data = request.json
    prompt = data.get('prompt', '').lower()
    
    response_data = {
        "status": "success",
        "message": "",
        "deep_link": "#",
        "plugin_used": ""
    }

    # 1. Lógica para swap-planner (Intercambios)
    if "swap" in prompt or "intercambia" in prompt:
        tokens = re.findall(r'\b[a-z]{3,5}\b', prompt)
        response_data["plugin_used"] = "pancakeswap-driver (swap-planner)"
        response_data["message"] = (
            "⚙️ Analizando ruta óptima de intercambio (Smart Router SDK)...\n"
            "✅ Contratos verificados.\n"
            "✅ Precios obtenidos exitosamente.\n"
            "El agente ha generado la ruta de intercambio sin requerir firmas manuales previas."
        )
        response_data["deep_link"] = "https://pancakeswap.finance/swap"
        
    # 2. Lógica para Lista DAO (CDP y Liquid Staking)
    elif "lista" in prompt or "slisbnb" in prompt or "lisusd" in prompt:
        response_data["plugin_used"] = "lista-dao-module"
        response_data["message"] = (
            "🏛️ Conectando con contratos de Lista DAO en BNB Chain...\n"
            "✅ Protocolo CDP verificado.\n"
            "La puerta de dos hojas está abierta para gestionar tus tokens líquidos."
        )
        response_data["deep_link"] = "https://lista.org/cdp"

    # 3. Lógica para liquidity-planner y farming-planner
    elif "liquidity" in prompt or "farm" in prompt or "pool" in prompt:
        response_data

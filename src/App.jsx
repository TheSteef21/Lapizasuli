import React, { useState, useEffect } from 'react';

// Fallback estático de telemetría base (Zona de Tránsito de Burunga)
const datosRespaldoLocal = {
  analisis_ia: "Análisis en modo local (Respaldo del Sistema). Telemetría base registrada con acumulado de eventos estable en la red de estaciones.",
  acumulado_total: 24,
  eventos: [
    {
      id: "SADV41-2026-A",
      ubicacion: "Zona de Subducción / Red de Estaciones USGS",
      pais_region: "Panamá",
      latitud: 7.0000,
      longitud: -82.5000,
      google_maps_url: "https://www.google.com/maps?q=7.0000,-82.5000",
      magnitud: 5.1,
      profundidad_km: 26.2,
      familia_redpy: "Familia Volcánica #04",
      coeficiente_correlacion: 0.89,
      fecha_hora: "2026-06-18 13:44:20"
    }
  ]
};

export default function App() {
  const mision = "SADV41";
  const BASE_URL = "https://lapizasuli.onrender.com";

  // --- ESTADOS DE LA MATRIZ (REACT CORE) ---
  const [sismos, setSismos] = useState(datosRespaldoLocal);
  const [isModoRespaldo, setIsModoRespaldo] = useState(true);
  const [isSincronizando, setIsSincronizando] = useState(false);
  
  // Estados Mecánicos (Turbo Tire)
  const [currentStyleClass, setCurrentStyleClass] = useState('tire-slick');
  const [sizeKnob, setSizeKnob] = useState(19);
  const [customBg, setCustomBg] = useState('');
  
  // Estados Web3 (Binance Llavero)
  const [walletAddress, setWalletAddress] = useState('');
  const [isWalletConnected, setIsWalletConnected] = useState(false);

  // --- REFRESCAR TELEMETRÍA (RENDER API) ---
  const refrescarMonitor = async () => {
    setIsSincronizando(true);
    try {
      const response = await fetch(`${BASE_URL}/api/sismos`);
      if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
      const data = await response.json();
      setSismos(data);
      setIsModoRespaldo(false);
    } catch (error) {
      console.warn("Falla en transmisión. Activando respaldo local controlado:", error);
      setSismos(datosRespaldoLocal);
      setIsModoRespaldo(true);
    } finally {
      setIsSincronizando(false);
    }
  };

  // Ciclo de Vida Automatizado (Efecto de consulta continua)
  useEffect(() => {
    refrescarMonitor();
    const interval = setInterval(refrescarMonitor, 60000);
    return () => clearInterval(interval);
  }, []);

  // --- LÓGICA DE ESCALA GEOMÉTRICA (TURBO TIRE) ---
  // Cálculo preciso: 15" = 42px base, 22" = 64px máx. Proporcional a pi.
  const calculatedPixels = 42 + ((sizeKnob - 15) * 3.14);

  const handleCustomCar = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => setCustomBg(e.target.result);
      reader.readAsDataURL(file);
    }
  };

  // --- ACCESO CONECTIVIDAD WEB3 ---
  const connectBinance = async () => {
    if (typeof window.ethereum !== 'undefined') {
      try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setWalletAddress(accounts[0]);
        setIsWalletConnected(true);
      } catch (error) {
        console.error("Conexión Web3 mitigada por el usuario.");
      }
    } else {
      alert("No se detectó un proveedor Web3 (Binance Wallet). Si estás en móvil, accede desde el navegador interno de tu Binance App.");
      window.open('https://web3.binance.com/en/referral?ref=ORCZSDLK', '_blank');
    }
  };

  const loginSocial = (provider) => console.log(`Social Auth: ${provider}`);

  return (
    <main className="min-h-screen bg-[#020617] text-[#f8fafc] font-sans relative overflow-hidden selection:bg-[#eab308] selection:text-[#020617] pb-12">
      
      {/* Estilos espectrales embebidos para compatibilidad nativa en GPU */}
      <style>{`
        .scanline {
          width: 100%; height: 2px; background: rgba(0, 209, 255, 0.1);
          position: fixed; z-index: 50; top: 0; pointer-events: none;
          animation: scanlineAnimation 8s linear infinite;
        }
        @keyframes scanlineAnimation { 0% { top: 0; } 100% { top: 100%; } }
        .text-shadow-oro { text-shadow: 0 0 10px rgba(234, 179, 8, 0.5); }
        .text-shadow-pink { text-shadow: 0 0 10px rgba(255, 42, 116, 0.6); }
        .text-shadow-blue { text-shadow: 0 0 10px rgba(0, 243, 255, 0.6); }
        .glass-panel {
          background: rgba(10, 10, 20, 0.75); backdrop-filter: blur(12px);
          border: 1px solid rgba(0, 209, 255, 0.3); position: relative; overflow: hidden;
        }
        .glass-panel::before {
          content: ""; position: absolute; top: 0; left: 0; width: 4px; height: 100%;
          background: #00D1FF; box-shadow: 0 0 10px #00D1FF;
        }
        .chassis-viewport {
          position: relative; width: 100%; height: 170px;
          background: rgba(5, 5, 10, 0.6); border: 1px dashed rgba(0, 209, 255, 0.25);
          background-size: cover; background-position: center;
        }
        .tire-profile {
          border-radius: 50%; background: radial-gradient(circle, rgba(0,0,0,0.85) 30%, rgba(20,20,30,0.95) 70%);
          box-shadow: 0 0 12px rgba(0, 209, 255, 0.3); display: flex; align-items: center; justify-content: center;
          animation: tireSpinAnimation 3s linear infinite;
        }
        @keyframes tireSpinAnimation { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .tire-slick { border: 4px solid #00D1FF; }
        .tire-semi { border: 5px double #FF00E5; }
        .tire-wet { border: 4px dashed #FFB800; }
        .rim-lines {
          width: 80%; height: 80%; border-radius: 50%; border: 1px dashed rgba(0, 255, 255, 0.5); position: relative;
        }
        .rim-lines::before, .rim-lines::after {
          content: ''; position: absolute; background: rgba(0, 255, 255, 0.4); top: 50%; left: 50%; transform: translate(-50%, -50%);
        }
        .rim-lines::before { width: 100%; height: 1px; }
        .rim-lines::after { width: 1px; height: 100%; }
        .knob-slider { -webkit-appearance: none; width: 100%; background: transparent; }
        .knob-slider::-webkit-slider-runnable-track { width: 100%; height: 6px; background: rgba(0, 209, 255, 0.15); border-radius: 3px; border: 1px solid rgba(0, 209, 255, 0.3); }
        .knob-slider::-webkit-slider-thumb { height: 16px; width: 16px; border-radius: 50%; background: #FF00E5; cursor: pointer; -webkit-appearance: none; margin-top: -5px; box-shadow: 0 0 8px #FF00E5; border: 2px solid #FFF; }
      `}</style>

      <div className="scanline"></div>

      {/* ==========================================
           ATRIO: ENTRADA Y ENCUENTRO DE LA PASARELA
           ========================================== */}
      <header class="fixed w-full z-50 bg-[#020617]/75 backdrop-blur-md border-b border-[#eab308]/30 px-6 py-4 flex flex-col md:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <span class="text-2xl">🛡️</span>
          <div>
            <h1 class="font-serif text-xl tracking-wider text-[#eab308] font-bold">SOVEREIGN HUB</h1>
            <p class="text-[9px] text-slate-400 font-mono tracking-widest">SADV41 VITE ARCHITECTURE</p>
          </div>
        </div>
        
        <nav class="flex gap-6 text-sm uppercase tracking-wider font-medium">
          <a href="#embassy-story" class="hover:text-pink-400 transition-colors text-pink-300">Embassy Story</a>
          <a href="#monitor-sismico-seccion" class="hover:text-red-400 transition-colors text-red-300 font-bold">⚠️ Telemetría</a>
          <a href="#probador-llantas-seccion" class="hover:text-cyan-400 transition-colors text-cyan-300">🛞 Turbo Tire</a>
          <a href="#mayordomia-seccion" class="hover:text-[#eab308] transition-colors text-amber-200">Mayordomía</a>
        </nav>

        <div class="flex flex-wrap gap-2 justify-center">
          <button onClick={() => loginSocial('google')} class="bg-white hover:bg-slate-200 text-slate-900 font-semibold text-xs px-3 py-2 rounded transition-all flex items-center gap-1.5 shadow cursor-pointer">🌐 Google Connect</button>
          <button onClick={() => loginSocial('github')} class="bg-slate-800 hover:bg-slate-700 text-white font-semibold text-xs px-3 py-2 rounded transition-all flex items-center gap-1.5 border border-slate-700 cursor-pointer">💻 GitHub Access</button>
          <button onClick={connectBinance} class={`${isWalletConnected ? 'bg-green-600 text-white' : 'bg-[#eab308] text-gray-950'} font-bold text-xs px-3 py-2 rounded transition-all flex items-center gap-1.5 shadow-lg cursor-pointer`}>
            {isWalletConnected ? '🌐 Connected' : '⚡ Binance Web3 Wallet'}
          </button>
        </div>
      </header>

      <main class="pt-36 pb-12 px-6 max-w-6xl mx-auto space-y-16">
        
        {/* WEBM3 PIPELINE LOG */}
        {isWalletConnected && (
          <div id="walletStatus" class="max-w-lg mx-auto p-4 bg-slate-900/90 border border-[#eab308]/40 rounded-xl font-mono shadow-2xl">
            <p class="text-[10px] text-slate-400 uppercase tracking-widest mb-1">⚡ Web3 Pipeline Active</p>
            <p class="text-xs text-slate-300 break-all">Dirección: <span class="text-[#eab308] font-bold select-all">{walletAddress}</span></p>
          </div>
        )}

        {/* ==========================================
             SANTO: EL PROCESO Y EXPRESIONES DE GRACIA
             ========================================== */}
        <section id="embassy-story" class="glass rounded-2xl overflow-hidden border border-pink-500/30 shadow-2xl max-w-lg mx-auto">
          <div class="p-8 text-center border-b border-white/5 bg-gradient-to-b from-pink-500/10 to-transparent">
            <h2 class="font-serif text-2xl md:text-3xl text-white font-extrabold tracking-wider text-shadow-pink uppercase">GSADV41: EMBASSY OF BEAUTY</h2>
            <p class="text-[#eab308] font-semibold text-sm tracking-widest mt-1 uppercase">6 Expressions of Sisterhood & Grace</p>
          </div>

          <div class="p-6 space-y-4 bg-slate-950/40 text-xs">
            <div class="bg-white/[0.02] border-l-4 border-[#ff2a74] p-4 rounded-r-xl">
              <div class="flex justify-between font-bold text-white mb-1"><span>The Emergency Therapist</span><span class="text-[#eab308]">Consuelo</span></div>
              <p class="text-slate-400">Te recibe con empatía divina, te seca las lágrimas y te recuerda el valor real de tu corona.</p>
            </div>
            <div class="bg-white/[0.02] border-l-4 border-[#00f3ff] p-4 rounded-r-xl">
              <div class="flex justify-between font-bold text-white mb-1"><span>The Beauty Ambassador</span><span class="text-[#eab308]">Generosidad</span></div>
              <p class="text-slate-400">Despliega un tocador impecable para ofrecer retoques de gracia y elegancia sin costo.</p>
            </div>
            <div class="bg-white/[0.02] border-l-4 border-[#ff2a74] p-4 rounded-r-xl">
              <div class="flex justify-between font-bold text-white mb-1"><span>The 5-Minute Sister</span><span class="text-[#eab308]">Conexión</span></div>
              <p class="text-slate-400">Admiración mutua y genuina de pasarela; un choque de palmas y un lazo digital instantáneo.</p>
            </div>
            <div class="bg-white/[0.02] border-l-4 border-[#00f3ff] p-4 rounded-r-xl">
              <div class="flex justify-between font-bold text-white mb-1"><span>The Search Squadron</span><span class="text-[#eab308]">Resguardo</span></div>
              <p class="text-slate-400">Activación inmediata y solidaria ante el llamado de alerta para proteger a la compañera.</p>
            </div>
            <div class="bg-white/[0.02] border-l-4 border-[#ff2a74] p-4 rounded-r-xl">
              <div class="flex justify-between font-bold text-white mb-1"><span>The Mirror Visionary</span><span class="text-[#eab308]">Esencia</span></div>
              <p class="text-slate-400">Captura la luz, la sofisticación y el encuadre perfecto de la hermandad en el espejo.</p>
            </div>
            <div class="bg-white/[0.02] border-l-4 border-[#00f3ff] p-4 rounded-r-xl">
              <div class="flex justify-between font-bold text-white mb-1"><span>The Dancefloor Philosopher</span><span class="text-[#eab308]">Propósito</span></div>
              <p class="text-slate-400">Sabiduría pura de pista que inspira a levantar la frente y celebrar la vida con plenitud.</p>
            </div>
          </div>
        </section>

        {/* TELEMETRÍA SÍSMICA MODULE (SADV41T) */}
        <section id="monitor-sismico-seccion" class="max-w-3xl mx-auto p-4 md:p-6 bg-[#0d1117] border border-slate-800 rounded-2xl shadow-xl">
          <div class="text-center py-2">
            <h2 class="text-[#da3637] font-bold text-2xl uppercase tracking-tight">Módulo SADV41T</h2>
            <p class="text-slate-400 text-xs mt-1 border-b border-slate-800 pb-4">Análisis de Estaciones y Multipletes Repetitivos</p>
          </div>

          <div class="flex justify-center items-center gap-4 my-4">
            <button class="bg-[#ff6b81] hover:bg-[#ff4757] text-white font-bold text-sm px-5 py-2 rounded-lg transition-all active:scale-95 cursor-pointer" onClick={refrescarMonitor}>
              {isSincronizando ? "Sincronizando..." : "Refrescar Monitor"}
            </button>
            <div class={`border px-4 py-1.5 rounded-full font-bold text-xs tracking-wide ${isModoRespaldo ? 'bg-red-500/10 text-[#da3637] border-red-500/40' : 'bg-green-500/10 text-green-400 border-green-500/40'}`}>
              {isModoRespaldo ? "Modo Respaldo" : "Sincronizado"}
            </div>
          </div>

          {isModoRespaldo && (
            <div class="bg-red-500/10 border border-red-500 rounded-xl p-4 text-xs text-left mb-4">
              <span class="font-bold text-red-500 block mb-1">⚠️ Enlace Alterno Operativo:</span>
              <p class="text-slate-300">Ruta proxy de Render temporalmente en cold start o inaccesible. Desplegando el respaldo estructural de la estación.</p>
            </div>
          )}

          {/* RENDERING DE ENTRADAS SÍSMICAS */}
          <div class="space-y-4 mt-6">
            <div class="bg-[#161b22] border border-slate-800 rounded-xl p-5 text-left">
              <div class="flex justify-between items-center mb-2">
                <h4 class="text-[#58a6ff] font-bold text-sm">🤖 Diagnóstico Analítico:</h4>
                <span class="text-[10px] bg-slate-800 px-2 py-0.5 rounded font-mono text-slate-400">Total: {sismos.acumulado_total}</span>
              </div>
              <p class="text-xs text-slate-300 font-mono leading-relaxed">{sismos.analisis_ia}</p>
            </div>

            {sismos.eventos && sismos.eventos.map((sismo) => (
              <div key={sismo.id} class="sismo-card border-l-4 border-rose-500 p-4 rounded-r-xl text-left bg-slate-950/50 border border-y-slate-800 border-r-slate-800">
                <div class="text-xs text-slate-200 font-semibold mb-1 flex justify-between items-center">
                  <span>📍 Ubicación: <span class="text-white">{sismo.ubicacion} ({sismo.pais_region})</span></span>
                  <a href={sismo.google_maps_url} target="_blank" rel="noreferrer" class="text-blue-400 hover:underline text-[10px] font-mono">Ver Mapa</a>
                </div>
                <div class="text-xs text-slate-400 grid grid-cols-2 gap-y-1 font-mono">
                  <div>📊 Magnitud: <span class="text-rose-400 font-bold">M {sismo.magnitud}</span></div>
                  <div>📉 Profundidad: <span class="text-cyan-400 font-bold">{sismo.profundidad_km} km</span></div>
                  <div class="col-span-2">🧬 Patrón REDPy: <span class="text-amber-400">{sismo.familia_redpy}</span> (CC: {sismo.coeficiente_correlacion})</div>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* ==========================================
             SANTÍSIMO: GEOMETRÍA MECÁNICA (TURBO TIRE)
             ========================================== */}
        <section id="probador-llantas-seccion" class="max-w-md mx-auto glass-panel p-6 rounded-2xl shadow-xl">
          <div class="text-center mb-4">
            <h3 class="bloom-text-blue font-mono text-sm uppercase tracking-widest font-bold text-[#00f3ff]">SADV41 Turbo Tire Viewport</h3>
            <p class="text-[10px] text-slate-400 font-mono mt-1">Simulación y Calibración en Caliente</p>
          </div>
          
          <div id="viewportBg" class="chassis-viewport rounded-xl flex items-center justify-center gap-8 overflow-hidden rotating-mesh" style={{ backgroundImage: customBg ? `url(${customBg})` : 'none' }}>
            <div id="hologramWrapper" class="flex gap-12 transition-opacity duration-300" style={{ opacity: customBg ? 0.25 : 1 }}>
              <div id="tire-front" class={`tire-profile ${currentStyleClass}`} style={{ width: `${calculatedPixels}px`, height: `${calculatedPixels}px` }}><div class="rim-lines"></div></div>
              <div id="tire-rear" class={`tire-profile ${currentStyleClass}`} style={{ width: `${calculatedPixels}px`, height: `${calculatedPixels}px` }}><div class="rim-lines"></div></div>
            </div>
          </div>

          <div class="mt-4 space-y-4">
            <div class="flex justify-between items-center text-xs font-mono px-1">
              <span class="text-slate-400">Dimensión de Rin Evaluada:</span>
              <span id="metricDisplay" class="text-[#eab308] font-bold text-shadow-oro text-sm">{sizeKnob}"</span>
            </div>
            
            <input type="range" id="sizeKnob" min="15" max="22" value={sizeKnob} class="knob-slider" onInput={(e) => setSizeKnob(parseInt(e.target.value))} />
            
            <div class="grid grid-cols-3 gap-2 pt-2">
              <button onClick={() => changeTire('tire-slick')} class="bg-slate-950 border border-[#00D1FF] text-[#00D1FF] hover:bg-cyan-950/30 text-[10px] font-mono py-1.5 rounded transition-all">Slick (Seco)</button>
              <button onClick={() => changeTire('tire-semi')} class="bg-slate-950 border border-[#FF00E5] text-[#FF00E5] hover:bg-purple-950/30 text-[10px] font-mono py-1.5 rounded transition-all">Semi-Slick</button>
              <button onClick={() => changeTire('tire-wet')} class="bg-slate-950 border border-[#FFB800] text-[#FFB800] hover:bg-amber-950/30 text-[10px] font-mono py-1.5 rounded transition-all">Wet (Lluvia)</button>
            </div>

            <div class="pt-1">
              <label class="bg-slate-900 border border-slate-700 hover:border-[#00f3ff] text-slate-300 text-center text-xs font-mono py-2 px-4 rounded block cursor-pointer transition-all">
                📷 Proyectar Chasis Externo
                <input type="file" class="hidden" accept="image/*" onChange={handleCustomCar} />
              </label>
            </div>
          </div>
        </section>

        {/* MAYORDOMÍA & REPOSITORIO DESCENTRALIZADO */}
        <section id="mayordomia-seccion" class="max-w-3xl mx-auto p-6 bg-[#0a0f1d] border border-gray-800 rounded-2xl shadow-xl space-y-4">
          <h2 class="text-2xl font-bold border-l-4 border-[#eab308] pl-3 text-white font-serif">Administración Espiritual y Provisión</h2>
          <p class="text-xs text-slate-300 leading-relaxed font-sans">
            La riqueza de la **SADV41** radica en la alineación entre la tecnología y un propósito eterno. Vinculamos herramientas Web3 con una visión clara de mayordomía, operando fuera de las presiones de escasez del sistema tradicional.
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
            <div class="bg-black p-4 rounded-xl border border-gray-800 font-mono text-[11px] text-green-400 shadow-inner">
              <p class="text-gray-500"># Sincronización del Hub de Habilidades</p>
              <p class="text-white"><span class="text-[#eab308]">$</span> npx skills add binance-web3</p>
            </div>
            <div class="bg-gray-950 p-4 rounded-xl border border-gray-800 flex flex-col justify-center">
              <h4 class="text-[10px] font-semibold uppercase tracking-wider text-slate-400 mb-1">Gobernanza Oficial (StevenDiorOficial)</h4>
              <p class="font-mono text-xs text-[#eab308] break-all select-all">0x59cB5992c35d6cD0fE6Ea94436c6AAE41F6E5fDD</p>
            </div>
          </div>
        </section>

        {/* ANCLADO SOBERANO DE RED */}
        <section class="glass rounded-2xl max-w-lg mx-auto overflow-hidden border border-cyan-500/30 text-center p-6 bg-black/30 flex flex-col items-center gap-4">
          <div class="border border-[#00f3ff]/40 px-4 py-1.5 rounded-full text-xs font-bold text-[#00f3ff] tracking-wide text-shadow-blue shadow-[0_0_10px_rgba(0,243,255,0.15)] uppercase">
            CONFESIONARIO DE GRACIA & ALERTAS GLOBALES
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 w-full px-4">
            <a href="https://wa.me/+15556670579" target="_blank" rel="noreferrer" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs px-4 py-2.5 rounded-lg transition-all shadow flex items-center justify-center gap-1.5 cursor-pointer">💬 Contactar IA SADV41</a>
            <a href="https://www.instagram.com/reel/DZNKr6Sla4M/?igsh=bDUzODcwanlyZWp6" target="_blank" rel="noreferrer" class="bg-gradient-to-r from-purple-600 to-pink-600 text-white font-semibold text-xs px-4 py-2.5 rounded-lg transition-all shadow flex items-center justify-center gap-1.5 cursor-pointer">📸 Ver Reel Instagram</a>
            <a href="https://www.meta.ai/@stevendioroficial/post/MG4xH5QUPGu?open_in_meta_ai=true&song_id=1887147568642873&utm_source=android_meta_ai_sl" target="_blank" rel="noreferrer" class="bg-blue-600 hover:bg-blue-500 text-white font-semibold text-xs px-4 py-2.5 rounded-lg transition-all shadow flex items-center justify-center gap-1.5 cursor-pointer col-span-2">🤖 Leer Arquitectura en Meta AI</a>
          </div>
          <p class="text-[10px] font-mono text-slate-500 pt-2">Algoritmo de Pureza v2.26 — Djyordy ⚡ | Anclado en IPFS</p>
          <p class="text-xs uppercase tracking-[0.2em] text-amber-200 font-semibold font-mono animate-pulse mt-1">Cristo está por venir • Misión SADV41</p>
          <div class="text-2xl mt-1 animate-[pulse_2s_infinite]">🎚</div>
        </section>

      </main>
    </main>
  );

  function changeTire(tireClass) {
    setCurrentStyleClass(tireClass);
  }
}

import React, { useState } from 'react';

const RegistroGuerreroSADV41 = () => {
  const [nombre, setNombre] = useState('STEVEN GÓMEZ SERRANO');
  const [disciplina, setDisciplina] = useState('Boxeo Clásico (Rubén Guerra Flow)');
  const [estaCargando, setEstaCargando] = useState(false);

  const handleTransformacion = () => {
    setEstaCargando(true);
    // Simulación de "Procesamiento de Nodo"
    setTimeout(() => {
      setEstaCargando(false);
      window.print(); // Abre el diálogo de impresión para "Sellar" el certificado
    }, 1500);
  };

  return (
    <div className="min-h-screen bg-[#050505] text-white p-4 md:p-8 font-sans flex flex-col items-center" 
         style={{ backgroundImage: 'radial-gradient(circle at center, #111827 0%, #000000 100%)' }}>
      
      {/* Header con Estética Dark de Panamá Oeste */}
      <header className="mb-10 text-center">
        <h1 className="text-4xl md:text-6xl font-black tracking-tighter uppercase mb-2">
          RUBÉN GUERRA <span className="text-[#d4af37] drop-shadow-[0_0_10px_rgba(212,175,55,0.5)]">SADV41</span>
        </h1>
        <p className="text-blue-400 italic font-mono tracking-[0.2em] uppercase text-xs md:text-sm">
            Preparación Tripartita: Física • Mental • Espiritual
        </p>
      </header>

      <main className="w-full max-w-6xl grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
        
        {/* Lado Izquierdo: Formulario de Registro (Inputs) */}
        <section className="bg-gray-900/80 p-8 border-t-4 border-[#d4af37] rounded-b-lg shadow-2xl backdrop-blur-sm">
          <h2 className="text-2xl font-bold text-[#d4af37] mb-8 uppercase tracking-widest">Registro de Nuevo Guerrero</h2>
          
          <div className="space-y-6">
            <div>
              <label className="block text-[10px] uppercase text-gray-400 mb-2 font-bold">Nombre Completo (El Nodo)</label>
              <input 
                type="text" 
                className="w-full bg-black border border-gray-800 p-4 rounded focus:border-blue-500 outline-none text-xl font-bold transition-all"
                value={nombre}
                onChange={(e) => setNombre(e.target.value.toUpperCase())}
              />
            </div>

            <div>
              <label className="block text-[10px] uppercase text-gray-400 mb-2 font-bold">Disciplina de Combate</label>
              <select 
                className="w-full bg-black border border-gray-800 p-4 rounded focus:border-[#d4af37] outline-none text-white appearance-none"
                onChange={(e) => setDisciplina(e.target.value)}
              >
                <option>Boxeo Clásico (Rubén Guerra Flow)</option>
                <option>Full Contact / Kick Boxing</option>
                <option>Defensa Personal Disciplinaria</option>
              </select>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-[10px] uppercase text-gray-400 mb-2 font-bold">Ubicación</label>
                <div className="p-4 bg-black/50 border border-gray-900 text-gray-500 rounded text-sm uppercase">Burunga, Panamá Oeste</div>
              </div>
              <div>
                <label className="block text-[10px] uppercase text-gray-400 mb-2 font-bold">Estado</label>
                <div className="p-4 bg-black/50 border border-gray-900 text-gold-500 text-sm uppercase text-[#d4af37]">Pluscuamperfecta</div>
              </div>
            </div>

            <button 
              onClick={handleTransformacion}
              className={`w-full py-5 rounded font-black uppercase tracking-[0.3em] transition-all shadow-[0_0_20px_rgba(220,38,38,0.3)] 
                ${estaCargando ? 'bg-gray-700 animate-pulse' : 'bg-red-700 hover:bg-red-600 active:scale-95'}`}
            >
              {estaCargando ? 'Codificando Nodo...' : 'Iniciar Transformación (Amén)'}
            </button>
          </div>
          
          <footer className="mt-8 pt-6 border-t border-gray-800 flex justify-between items-center opacity-50">
            <span className="text-[9px] font-mono">ID: CHRIST(O)-BOX-89012251</span>
            <span className="text-[9px] font-mono uppercase tracking-widest">Verbo (1) Activado</span>
          </footer>
        </section>

        {/* Lado Derecho: Certificado Real Proyectado (Output) */}
        <section className="sticky top-8">
          <div className="w-full p-1 border-4 border-double border-[#d4af37] bg-black rounded shadow-[0_0_50px_rgba(0,0,0,1)]">
            <div className="border-2 border-yellow-900/30 p-8 text-center relative overflow-hidden bg-gradient-to-b from-gray-900 to-black">
              
              {/* Sello de Agua SADV41 */}
              <div className="absolute inset-0 flex items-center justify-center opacity-[0.03] pointer-events-none select-none">
                <span className="text-[12rem] font-black rotate-[-15deg]">SADV41</span>
              </div>

              <header className="flex justify-between items-start text-[9px] font-mono text-[#d4af37] mb-8 uppercase tracking-widest">
                <span>Estéreo: 2200W</span>
                <span>Fundación Artes Disciplinarias</span>
              </header>

              <h3 className="text-2xl font-serif text-[#d4af37] uppercase tracking-tighter mb-1">Certificado de Realeza</h3>
              <p className="text-[10px] text-blue-400 font-mono mb-8">Nivel III - Integración Empresarial y Deportiva</p>
              
              <p className="text-xs uppercase text-gray-500 mb-2">Se reconoce formalmente al Guerrero:</p>
              
              {/* Proyección Dinámica del Nombre */}
              <div className="relative inline-block px-8 py-2 mb-8">
                <h4 className="text-4xl md:text-5xl font-black text-white uppercase border-b-2 border-[#d4af37] pb-2 min-h-[60px]">
                  {nombre || '______'}
                </h4>
              </div>

              <div className="max-w-md mx-auto text-[11px] leading-relaxed text-gray-300 italic mb-10">
                "Por haber culminado el proceso de preparación tripartita, fusionando la disciplina física del {disciplina}, 
                la agudeza mental y el fortalecimiento espiritual bajo la sabiduría del Maestro Rubén Guerra."
              </div>

              <footer className="grid grid-cols-3 gap-4 items-end mt-6">
                <div className="text-center">
                  <div className="w-full border-b border-gray-700 mb-1"></div>
                  <p className="text-[8px] font-bold uppercase">Maestro Rubén Guerra</p>
                  <p className="text-[7px] text-[#d4af37]">Director Académico</p>
                </div>
                
                <div className="flex justify-center pb-1">
                   <div className="w-12 h-12 rounded-full border border-red-900 bg-red-950/30 flex items-center justify-center text-xl shadow-[0_0_15px_rgba(153,27,27,0.4)]">
                     🥊
                   </div>
                </div>

                <div className="text-center">
                  <div className="w-full border-b border-gray-700 mb-1"></div>
                  <p className="text-[8px] font-bold uppercase">Steven Dior</p>
                  <p className="text-[7px] text-[#d4af37]">SADV41 - Sello Real</p>
                </div>
              </footer>

              <p className="mt-8 text-[8px] font-mono text-gray-600 uppercase tracking-[0.4em]">
                Vista Previa de Egreso • Burunga 2026
              </p>
            </div>
          </div>
          <p className="text-center text-gray-500 text-[10px] mt-6 font-mono animate-pulse">
            SISTEMA LISTO PARA SELLAR E IMPRIMIR (AMÉN)
          </p>
        </section>

      </main>
    </div>
  );
};

export default RegistroGuerreroSADV41;

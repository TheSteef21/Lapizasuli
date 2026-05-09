import React, { useState, useEffect } from 'react';

const PortalGuerreroSADV41 = () => {
  const [nombre, setNombre] = useState('STEVEN GÓMEZ SERRANO');
  const [disciplina, setDisciplina] = useState('Boxeo Clásico (Rubén Guerra Flow)');
  const [contador, setContador] = useState(0);
  const [estaCargando, setEstaCargando] = useState(false);

  // Cargar contador desde persistencia local (Simulando base de datos SADV41)
  useEffect(() => {
    const totalRegistros = localStorage.getItem('contadorSADV41');
    if (totalRegistros) setContador(parseInt(totalRegistros));
  }, []);

  const handleRegistroFinal = () => {
    setEstaCargando(true);
    
    // Simulación de envío a sadv41@gmail.com y actualización de cuenta
    setTimeout(() => {
      const nuevoTotal = contador + 1;
      setContador(nuevoTotal);
      localStorage.setItem('contadorSADV41', nuevoTotal.toString());
      setEstaCargando(false);
      
      alert(`Nodo Registrado. Correo enviado a sadv41@gmail.com. Total Guerreros: ${nuevoTotal}`);
      window.print(); 
    }, 2000);
  };

  return (
    <div className="min-h-screen bg-[#050505] text-white p-4 md:p-8 font-sans flex flex-col items-center" 
         style={{ backgroundImage: 'radial-gradient(circle at center, #111827 0%, #000000 100%)' }}>
      
      {/* Header con Estética Dark y Glitch */}
      <header className="mb-10 text-center">
        <h1 className="text-4xl md:text-6xl font-black tracking-tighter uppercase mb-2 text-white" 
            style={{ textShadow: '2px 0 #ff0000, -2px 0 #0000ff' }}>
          RUBÉN GUERRA <span className="text-[#d4af37]">SADV41</span>
        </h1>
        <p className="text-blue-400 italic font-mono tracking-[0.2em] uppercase text-xs md:text-sm">
            Física • Mental • Espiritual | "Donde el 0 y el 1 se vuelven Vida"
        </p>
      </header>

      <main className="w-full max-w-6xl grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
        
        {/* Lado Izquierdo: Control y Canales de Pago */}
        <section className="bg-gray-900/80 p-8 border-t-4 border-[#d4af37] rounded-b-lg shadow-2xl backdrop-blur-sm">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-xl font-bold text-[#d4af37] uppercase">Registro de Nodo</h2>
            <div className="bg-black px-3 py-1 border border-blue-500 rounded font-mono text-blue-400 text-sm">
              GUERREROS: {contador.toString().padStart(4, '0')}
            </div>
          </div>
          
          <div className="space-y-6">
            <div>
              <label className="block text-[10px] uppercase text-gray-400 mb-2 font-bold">Identidad del Nodo</label>
              <input 
                type="text" 
                className="w-full bg-black border border-gray-800 p-4 rounded focus:border-blue-500 outline-none text-xl font-bold transition-all text-white"
                value={nombre}
                onChange={(e) => setNombre(e.target.value.toUpperCase())}
              />
            </div>

            <div>
              <label className="block text-[10px] uppercase text-gray-400 mb-2 font-bold">Alcurnia Deportiva</label>
              <select 
                className="w-full bg-black border border-gray-800 p-4 rounded focus:border-[#d4af37] outline-none text-white appearance-none"
                onChange={(e) => setDisciplina(e.target.value)}
              >
                <option>Boxeo Clásico (Rubén Guerra Flow)</option>
                <option>Full Contact / Kick Boxing</option>
                <option>Defensa Personal Disciplinaria</option>
              </select>
            </div>

            {/* Canales de Registro y Pago */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <a href="https://wa.me/message/GYU3IAM5KDXSB1" target="_blank" rel="noreferrer"
                 className="flex items-center justify-center gap-2 bg-green-900/30 border border-green-600 p-3 rounded hover:bg-green-600 transition text-xs font-bold uppercase">
                <span>💬 WhatsApp</span>
              </a>
              <a href="https://yappypa.page.link/Zi7X?hash=rjYRsJ8Yz0hGBKWXnNKRpeCr5yZZkbjbgkxGCAZdd/nmXoS0X8s5ntvwHrGm+7HT" target="_blank" rel="noreferrer"
                 className="flex items-center justify-center gap-2 bg-blue-900/30 border border-blue-600 p-3 rounded hover:bg-blue-600 transition text-xs font-bold uppercase text-white">
                <span>💳 Yappy</span>
              </a>
            </div>

            <button 
              onClick={handleRegistroFinal}
              className={`w-full py-5 rounded font-black uppercase tracking-[0.3em] transition-all shadow-[0_0_20px_rgba(220,38,38,0.3)] 
                ${estaCargando ? 'bg-gray-700 animate-pulse' : 'bg-red-700 hover:bg-red-600 active:scale-95'}`}
            >
              {estaCargando ? 'Sincronizando Correo...' : 'Registrar al SADV41 (Amén)'}
            </button>
          </div>
          
          <footer className="mt-8 pt-6 border-t border-gray-800 flex justify-between items-center opacity-50">
            <span className="text-[9px] font-mono">HASH: rjYRsJ8Yz0...7HT</span>
            <span className="text-[9px] font-mono uppercase tracking-widest text-[#d4af37]">Burunga 2026</span>
          </footer>
        </section>

        {/* Lado Derecho: Certificado Real Proyectado */}
        <section className="sticky top-8">
          <div className="w-full p-1 border-4 border-double border-[#d4af37] bg-black rounded shadow-[0_0_50px_rgba(0,0,0,1)]">
            <div className="border-2 border-yellow-900/30 p-8 text-center relative overflow-hidden bg-gradient-to-b from-gray-900 to-black">
              
              <div className="absolute inset-0 flex items-center justify-center opacity-[0.03] pointer-events-none select-none">
                <span className="text-[12rem] font-black rotate-[-15deg]">SADV41</span>
              </div>

              <header className="flex justify-between items-start text-[9px] font-mono text-[#d4af37] mb-8 uppercase tracking-widest">
                <span>ESTÉREO: 2200W</span>
                <span>ESC. RUBÉN GUERRA</span>
              </header>

              <h3 className="text-2xl font-serif text-[#d4af37] uppercase tracking-tighter mb-1">Certificado de Realeza</h3>
              <div className="w-24 h-px bg-[#d4af37] mx-auto mb-6"></div>
              
              <p className="text-[10px] text-gray-500 uppercase mb-2">Reconocimiento formal al Guerrero:</p>
              
              <div className="relative inline-block px-8 py-2 mb-8">
                <h4 className="text-3xl md:text-4xl font-black text-white uppercase border-b-2 border-[#d4af37] pb-2">
                  {nombre || '______'}
                </h4>
              </div>

              <div className="max-w-md mx-auto text-[10px] leading-relaxed text-gray-300 italic mb-10">
                "Bajo la ley de la Mora de Gracia, este nodo ha integrado la disciplina física del {disciplina} 
                con la preparación espiritual absoluta bajo la tutela del Maestro Rubén Guerra."
              </div>

              <footer className="grid grid-cols-3 gap-4 items-end mt-6">
                <div className="text-center">
                  <div className="w-full border-b border-gray-700 mb-1"></div>
                  <p className="text-[8px] font-bold uppercase">Maestro Guerra</p>
                  <p className="text-[6px] text-[#d4af37]">Académico</p>
                </div>
                <div className="flex justify-center pb-1">
                   <div className="w-10 h-10 rounded-full border border-red-900 bg-red-950/30 flex items-center justify-center text-lg">🥊</div>
                </div>
                <div className="text-center">
                  <div className="w-full border-b border-gray-700 mb-1"></div>
                  <p className="text-[8px] font-bold uppercase">Steven Dior</p>
                  <p className="text-[6px] text-[#d4af37]">Sello Real</p>
                </div>
              </footer>
            </div>
          </div>
          <p className="text-center text-gray-500 text-[10px] mt-6 font-mono uppercase tracking-widest">
            The Real Essence of Panamá Oeste
          </p>
        </section>

      </main>
    </div>
  );
};

export default PortalGuerreroSADV41;

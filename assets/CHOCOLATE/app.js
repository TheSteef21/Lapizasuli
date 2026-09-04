import React, { useState } from 'react';
import { 
  Hexagon, 
  Eye, 
  Flame, 
  Newspaper, 
  Users, 
  Crown, 
  Activity, 
  Briefcase, 
  Scale, 
  ExternalLink,
  ChevronRight,
  Phone,
  MapPin,
  Globe,
  Clock3,
  MessageCircle,
  ShieldCheck,
  Music,
  FolderOpen,
  Link as LinkIcon
} from 'lucide-react';

const laminasData = [
  {
    id: 13,
    isTrending: true,
    lamina: "LÁMINA COLECCIONABLE #13 - SADV41",
    category: "Sismo",
    title: "Terremoto de magnitud 6.3 sacude Alaska y alerta a Rusia",
    summary: "El USGS registró un sismo M 6.3 a 84 km de Nikolski, Islas Aleutianas. Sin probabilidad de pérdidas ni daños.",
    url: "https://www.threads.com/share/BADRm6gRrt/",
    type: "joke",
    surprise: "6.3 en Alaska... ¡allá hace tanto frío que hasta las placas tectónicas tiemblan, pero de hielo!"
  },
  {
    id: 14,
    isTrending: false,
    lamina: "LÁMINA COLECCIONABLE #14 - SADV41",
    category: "Economía",
    title: "Alza de Combustible: Nuevos precios",
    summary: "95 Octanos a B/. 1.281, 91 Octanos a B/. 1.197 y Diésel a B/. 1.403 en Arraiján y La Chorrera",
    url: "#",
    type: "joke",
    surprise: "Sube el combustible... ¡voy a tener que echarle agua al tanque y fe al motor!"
  },
  {
    id: 15,
    isTrending: false,
    lamina: "LÁMINA COLECCIONABLE #15 - SADV41",
    category: "Judicial",
    title: "Operación Credenciales I: Diplomas Falsos",
    summary: "Jueza ordena detención provisional para 10 imputados y casa por cárcel para otros 13",
    url: "#",
    type: "joke",
    isMurder: true, // Forzando el estilo oscuro/serio si se requiere
    surprise: "Diplomas falsos... ¡con razón hay tanto experto que no sabe ni prender la computadora!"
  },
  {
    id: 1,
    isTrending: true,
    lamina: "LÁMINA COLECCIONABLE #01 - SADV41",
    category: "Historia",
    title: "El Origen de la Logia Pluscuamperfecta",
    summary: "Documentos desclasificados revelan las primeras reuniones en la zona de Burunga.",
    url: "#",
    type: "bible",
    surprise: "Porque donde están dos o tres congregados en mi nombre, allí estoy yo en medio de ellos. Mateo 18:20"
  }
];

const LaminaCard = ({ lamina }) => {
  return (
    <div className={`group bg-[#111827] rounded-2xl overflow-hidden shadow-xl flex flex-col relative transition-all duration-300 hover:shadow-2xl hover:-translate-y-1 ${lamina.isTrending ? "border-2 border-red-500/60" : "border border-[#1F2937] hover:border-slate-700/80"}`}>
      
      {/* Header Shine */}
      <div className="relative overflow-hidden bg-gradient-to-r from-amber-300 to-yellow-500 text-[#0B0F19] px-4 py-2.5 flex items-center justify-between shadow-[inset_0_1px_0_rgba(255,255,255,0.5),_inset_0_-1px_0_rgba(0,0,0,0.2),_0_2px_8px_rgba(0,0,0,0.3)] backdrop-saturate-125">
        <div className="absolute top-0 -left-full w-[60%] h-full bg-gradient-to-r from-transparent via-white/60 to-transparent -skew-x-12 animate-[shineMove_3.2s_ease-in-out_infinite]" />
        <span className="text-[10px] font-black tracking-widest uppercase truncate pr-2 z-10">{lamina.lamina}</span>
        <span className="text-[10px] shrink-0 z-10">✨🍫</span>
        {lamina.isTrending && (
          <div className="absolute -top-2 -right-2 bg-red-600 text-white text-[9px] font-black px-2.5 py-1 rounded-full flex items-center gap-1 shadow-[0_0_0_0_rgba(239,68,68,0.4)] animate-[pulseGold_2s_infinite]">
            <Crown className="w-3 h-3" />
            #1 EN TENDENCIA
          </div>
        )}
      </div>

      {/* Surprise Box */}
      <div className={`px-5 py-4 border-b flex flex-col items-center justify-center min-h-[92px] ${lamina.isMurder ? "bg-slate-900/80 border-slate-800" : "bg-slate-900/60 border-slate-800"}`}>
        {lamina.type === "joke" ? (
          <div className="text-center w-full">
            <div className="text-[11px] font-bold tracking-widest uppercase text-amber-300/80 mb-2">😂 Chiste del día</div>
            <p className="text-slate-100 italic text-[13px] leading-relaxed font-medium line-clamp-4">"{lamina.surprise}"</p>
          </div>
        ) : (
          <div className="text-center w-full">
            <div className="text-[11px] font-bold tracking-widest uppercase text-emerald-300/80 mb-2">✝️ Versículo Bíblico</div>
            <p className="text-slate-200 italic text-[12px] leading-relaxed">{lamina.surprise}</p>
          </div>
        )}
      </div>

      {/* Body */}
      <div className="p-5 flex-grow flex flex-col">
        <span className="text-[10px] font-bold tracking-widest uppercase text-slate-500 mb-2">{lamina.category}</span>
        <a href={lamina.url} target="_blank" rel="noopener noreferrer" className="font-bold text-white text-[14px] leading-tight hover:text-amber-200 transition line-clamp-3">
          {lamina.title}
        </a>
        <p className="text-[12px] text-slate-400 mt-2 leading-relaxed line-clamp-2">{lamina.summary}</p>

        <div className="mt-4">
          <a href={lamina.url} target="_blank" rel="noopener noreferrer" className={`w-full inline-flex items-center justify-center gap-2 font-bold py-3 px-4 rounded-xl text-[13px] transition shadow-lg ${lamina.isMurder ? "bg-gradient-to-r from-slate-700 to-slate-600 hover:from-slate-600 hover:to-slate-500 text-white" : lamina.isTrending ? "bg-gradient-to-r from-amber-400 to-yellow-500 hover:from-amber-300 hover:to-yellow-400 text-[#0B0F19]" : "bg-gradient-to-r from-emerald-600 to-teal-500 hover:from-emerald-500 hover:to-teal-400 text-white"}`}>
            🍫 Destapar Chocolate → Leer Fuente
            <ExternalLink className="w-4 h-4" />
          </a>
        </div>

        <div className="mt-4 pt-3 border-t border-slate-800/60 flex flex-col gap-2">
          <p className="text-[11px] italic text-emerald-300/80">¿Pa'eso tú quieres andar leyendo y enterándote de todo? 🗿🔐</p>
          <span className="text-[10px] font-bold text-amber-300/90 self-end">atte: SADV41 🗿🤙🏼🇵🇦🏁</span>
        </div>
      </div>
    </div>
  );
};

const AtrioSection = () => (
  <div className="space-y-12 animate-in fade-in duration-500">
    <section className="space-y-6">
      <div className="text-center max-w-3xl mx-auto pt-2">
        <h1 className="text-[24px] sm:text-4xl font-black tracking-tight text-white leading-tight">
          🗿 Enmarcando a los #1 - Noticias del Día con Lámina de Chocolate SADV41 🏁
        </h1>
        <p className="text-slate-400 text-[13px] sm:text-[14px] mt-3 leading-relaxed max-w-2xl mx-auto">
          Cada noticia trae su lámina coleccionable como chocolates de plástico. Primero ríes o reflexionas, luego destapas y lees fuente. atte: SADV41 🗿🤙🏼🇵🇦🏁
        </p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-5 sm:gap-6">
        {laminasData.map(lamina => (
          <LaminaCard key={lamina.id} lamina={lamina} />
        ))}
      </div>
    </section>
  </div>
);

const SantoSection = () => (
  <section className="bg-[#111827] border border-[#1F2937] rounded-2xl p-6 sm:p-8 shadow-xl relative overflow-hidden animate-in fade-in duration-500">
    <div className="flex items-start gap-3 mb-7">
      <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-purple-600 to-pink-500 flex items-center justify-center text-white shrink-0">
        <Users className="w-5 h-5" />
      </div>
      <div>
        <span className="text-[11px] font-semibold text-purple-300 uppercase tracking-widest">Cuaderno de Notas del Día - Comunidad</span>
        <h2 className="text-[20px] font-bold text-white mt-0.5">Comunidad & Beneficios SADV41</h2>
        <p className="text-[12px] text-slate-400 mt-1">Links verificados • Sin caducidad • Burunga District</p>
      </div>
    </div>

    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
      <a href="https://tiktok.me/group/ZSqdyEx5s/" target="_blank" rel="noopener noreferrer" className="group bg-slate-900/70 border border-slate-800 rounded-xl p-5 hover:border-cyan-500/40 transition flex flex-col gap-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-black to-cyan-500 flex items-center justify-center text-white border border-white/10">
              <span className="font-black text-[12px]">TT</span>
            </div>
            <div>
              <p className="text-[10px] font-bold tracking-widest uppercase text-cyan-300">TIKTOK GROUP</p>
              <h3 className="font-bold text-white text-[13px] leading-tight">Burunga District - Grupo TikTok</h3>
            </div>
          </div>
          <ExternalLink className="w-4 h-4 text-slate-500 group-hover:text-cyan-300" />
        </div>
        <p className="text-[12px] text-slate-400">Únete al distrito. Noticias, chistes y láminas en tiempo real.</p>
        <div className="inline-flex items-center gap-2 text-[11px] font-bold text-cyan-300 bg-cyan-500/10 border border-cyan-500/20 rounded-full px-3 py-1 w-fit">
          <span className="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse" /> Invitación activa
        </div>
      </a>
      
      <a href="https://thesteef21.github.io/Lapizasuli/assets/CONTACTOS/index.html" target="_blank" rel="noopener noreferrer" className="group bg-slate-900/70 border border-slate-800 rounded-xl p-5 hover:border-emerald-500/40 transition flex flex-col gap-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 flex items-center justify-center text-white">
              <FolderOpen className="w-5 h-5" />
            </div>
            <div>
              <p className="text-[10px] font-bold tracking-widest uppercase text-emerald-300">PORTAL ACTIVO</p>
              <h3 className="font-bold text-white text-[13px] leading-tight">Directorio Unificado</h3>
            </div>
          </div>
          <ExternalLink className="w-4 h-4 text-slate-500 group-hover:text-emerald-300" />
        </div>
        <p className="text-[12px] text-slate-400">Versión desplegada actual del directorio TheSteef21 / Lapizasuli.</p>
      </a>
    </div>
  </section>
);

const SantisimoSection = () => (
  <section className="bg-[#111827] border border-[#1F2937] rounded-2xl p-6 sm:p-8 shadow-xl relative overflow-hidden animate-in fade-in duration-500">
    <div className="flex items-start gap-3 mb-6">
      <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 flex items-center justify-center text-white shrink-0">
        <Hexagon className="w-5 h-5" />
      </div>
      <div>
        <span className="text-[11px] font-semibold text-emerald-400 uppercase tracking-widest">Lo que escribí el día que creé el cuaderno</span>
        <h2 className="text-[20px] font-bold text-white mt-0.5">El Santísimo - Sovereign Core</h2>
      </div>
    </div>
    
    <div className="space-y-3 text-slate-300 text-[13px] leading-relaxed border-l-2 border-emerald-500/40 pl-4 sm:pl-6">
      <p><strong className="text-white">1</strong> Palabras de bendición con las que bendijo Enoc a los elegidos justos que vivirán en el día de la tribulación...</p>
      <p><strong className="text-white">2</strong> Enoc, hombre justo a quien le fue revelada una visión del Santo y del cielo...</p>
      <p><strong className="text-white">8</strong> Pero con los justos Él hará la paz y protegerá a los elegidos...</p>
      <p><strong className="text-white">9</strong> Mirad que Él viene con una multitud de sus santos, para ejecutar el juicio sobre todos...</p>
    </div>
  </section>
);

export default function App() {
  const [activeTab, setActiveTab] = useState('atrio');

  return (
    <div className="min-h-screen bg-[#0B0F19] text-slate-100 font-sans selection:bg-emerald-500 selection:text-white flex flex-col relative overflow-x-hidden">
      
      {/* Background Ambience */}
      <div className="pointer-events-none fixed inset-0 z-0 overflow-hidden">
        <div className="absolute -top-20 -left-20 w-[380px] h-[380px] bg-emerald-500/10 rounded-full blur-[80px]" />
        <div className="absolute top-[30%] -right-20 w-[380px] h-[380px] bg-blue-500/10 rounded-full blur-[80px]" />
        <div className="absolute bottom-0 left-1/3 w-[500px] h-[300px] bg-amber-500/5 rounded-full blur-[90px]" />
      </div>
      
      {/* Header */}
      <header className="relative z-10 border-b border-[#1F2937] bg-[#0B0F19]/80 backdrop-blur-md sticky top-0">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-[72px] sm:h-20 flex items-center justify-between gap-4">
          <div className="flex items-center gap-3 min-w-0">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 to-teal-400 flex items-center justify-center shadow-lg shadow-emerald-500/20 shrink-0">
              <span className="text-lg">🗿</span>
            </div>
            <div className="min-w-0">
              <span className="text-[16px] sm:text-[18px] font-extrabold tracking-tight text-white block leading-none truncate">
                Ecosistema Unificado
              </span>
              <span className="block text-[10px] sm:text-[11px] text-emerald-400 font-medium tracking-widest uppercase mt-1 truncate">
                SpatiX • Steven Dior • Gnimport 🗿🤙🏼🇵🇦🏁
              </span>
            </div>
          </div>
          <div className="hidden sm:flex items-center gap-2 bg-slate-800/80 border border-slate-700/60 px-3 py-1.5 rounded-full text-xs font-medium text-emerald-400 shrink-0">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" /> Red Global Activa
          </div>
        </div>
      </header>

      <main className="relative z-10 flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8 w-full">
        
        {/* Navigation */}
        <div className="flex flex-col sm:flex-row justify-center space-y-2 sm:space-y-0 sm:space-x-4 mb-8">
          {[
            { id: 'atrio', label: 'El Atrio', icon: Newspaper, activeColor: 'text-emerald-400 border-emerald-400 bg-emerald-950/30' },
            { id: 'santo', label: 'Lugar Santo', icon: Users, activeColor: 'text-cyan-400 border-cyan-400 bg-cyan-950/30' },
            { id: 'santisimo', label: 'El Santísimo', icon: Crown, activeColor: 'text-amber-400 border-amber-400 bg-amber-950/30' }
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`flex items-center justify-center space-x-2 px-6 py-3 rounded-lg border border-[#1F2937] bg-[#111827] font-medium transition-all duration-300 ${activeTab === tab.id ? tab.activeColor : 'text-slate-400 hover:text-slate-200 hover:border-slate-700'}`}
            >
              <tab.icon className="w-5 h-5" />
              <span>{tab.label}</span>
              {activeTab === tab.id && <ChevronRight className="w-4 h-4 ml-2 opacity-50" />}
            </button>
          ))}
        </div>

        {/* Content Area */}
        <div className="min-h-[500px]">
          {activeTab === 'atrio' && <AtrioSection />}
          {activeTab === 'santo' && <SantoSection />}
          {activeTab === 'santisimo' && <SantisimoSection />}
        </div>

      </main>

      <footer className="relative z-10 border-t border-[#1F2937] bg-[#0B0F19] py-8 mt-6">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-3">
          <p className="text-emerald-400 font-bold text-[16px]">¿Pa'eso tú quieres andar leyendo y enterándote de todo? 🗿🔐</p>
          <p className="text-[11px] text-slate-500">© 2026 Steven Dior Oficial • SpatiX RTK • Gnimport. Todos los derechos reservados. atte: SADV41 🗿🤙🏼🇵🇦🏁</p>
        </div>
      </footer>
    </div>
  );
}

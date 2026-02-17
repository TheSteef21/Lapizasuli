import React from 'react';
import './restauracion.css'; // El CSS para la estética y las 'mañas'

const Restauracion = () => {
  // Aquí podemos definir lógica de estado o props si fuera una aplicación más compleja
  // Por ahora, es una representación de la estructura que te importa

  const handleCitaChange = (e) => {
    const val = e.target.value.toLowerCase();
    if (val.includes('colosenses 3:3') || val.includes('colosenses 3 3')) {
      // Aquí se activaría la lógica de "¡VIVE!" y el envío de correo
      console.log("¡VIVE! Activado. Enviando notificación a madcom21@gmail.com");
      alert("¡VIVE! Tu alma ha reconocido la frecuencia. Notificación enviada a Steven."); // Simulación para el usuario
    }
  };

  return (
    <div className="restauracion-body">
      <header className="restauracion-header">
        <h1 className="restauracion-title">Steven Dior</h1>
        <p className="restauracion-subtitle">Misión SADV41 • Protocolo Génesis</p>
      </header>

      <main className="restauracion-main">
        {/* Catálogo de Servicios - La Siembra */}
        <a href="https://take.app/stevendior" target="_blank" className="restauracion-button catalogo">
          <span>🛍️ Catálogo de Servicios</span>
          <span className="subtitle">Fecundando Oportunidades</span>
        </a>

        {/* Terminal MetaF - El Corazón de la Restauración */}
        <a href="/metaf.html" className="restauracion-button metaf">
          <span>🏛️ Terminal MetaF</span>
          <span className="subtitle">Soberanía de Identidad</span>
        </a>

        {/* Linktree Original - El Recuerdo del Camino */}
        <a href="https://linktr.ee/stevendior" target="_blank" className="restauracion-button linktree">
          <span>🔗 Linktree Original</span>
          <span className="subtitle">El Camino Recorrido</span>
        </a>

        {/* Yahoo Intelligence - La Visión del Presente */}
        <div className="restauracion-info yahoo-intel">
          <p className="title">Noticias del Satélite</p>
          <p className="subtitle italic">
            "Sincronizando el granito de arena informativo para Panamá..."
          </p>
        </div>

        {/* El Nodo Invisible - La Semilla Activa */}
        <div className="restauracion-info nodo-invisible">
          <p className="title">El Nodo Invisible</p>
          <p className="subtitle">
            Si estás aquí, escribe la cita que te trae.
          </p>
          <input 
            type="text" 
            placeholder="Escribe Colosenses 3:3" 
            className="restauracion-input" 
            onChange={handleCitaChange} 
          />
          <div className="response-area" id="respuesta-restauracion">
            {/* Aquí aparecerá el ¡VIVE! */}
          </div>
        </div>
      </main>

      <footer className="restauracion-footer">
        <p className="footer-contact">madcom21@gmail.com • 0xcff...B7EF</p>
        <p className="footer-location">Burunga • 2026</p>
        <p className="footer-genesis">. </p> {/* El punto que representa Génesis 1 */}
      </footer>
    </div>
  );
};

export default Restauracion;

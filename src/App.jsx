import React from 'react';
import './styles/global.css';

const App = () => {
  const mision = "SADV41";

  return (
    <main className="tabernaculo-container">
      <header className="atrio-header">
        <h1>{mision}</h1>
        <p className="vision-text">De la unión nace la fuerza, de la trinidad la visión.</p>
      </header>

      <section className="santo-content">
        <div className="card-reflejo">
          <h2>Misión de Servicio</h2>
          <p>Transformando el caos en orden perfecto.</p>
          <span className="symbol-vocal">🎚</span>
        </div>
      </section>

      <footer className="santisimo-footer">
        <p>Cristo está por venir • Misión SADV41</p>
      </footer>
    </main>
  );
};

export default App;

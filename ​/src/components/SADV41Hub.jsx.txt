import React, { useEffect, useRef, useState } from 'react';
import { MapContainer, TileLayer, Polyline } from 'react-leaflet';
import { Pose, POSE_CONNECTIONS } from '@mediapipe/pose';
import * as cam from '@mediapipe/camera_utils';
import 'leaflet/dist/leaflet.css';

const SADV41Hub = () => {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [trayectoria, setTrayectoria] = useState([[8.9167, -79.6667]]); // Burunga, Panamá

  // 1. Integración de Visión Artificial (Anatomía/Artes Marciales)
  const onResults = (results) => {
    const canvasElement = canvasRef.current;
    const canvasCtx = canvasElement.getContext('2d');
    canvasCtx.save();
    canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
    canvasCtx.drawImage(results.image, 0, 0, canvasElement.width, canvasElement.height);
    
    // Dibujo de postura anatómica para corrección de técnica
    if (results.poseLandmarks) {
      window.drawConnectors(canvasCtx, results.poseLandmarks, POSE_CONNECTIONS, {color: '#d4af37', lineWidth: 4});
      window.drawLandmarks(canvasCtx, results.poseLandmarks, {color: '#00ff41', lineWidth: 2});
    }
    canvasCtx.restore();
  };

  useEffect(() => {
    const pose = new Pose({locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/pose/${file}`});
    pose.setOptions({ modelComplexity: 1, smoothLandmarks: true, minDetectionConfidence: 0.5 });
    pose.onResults(onResults);

    if (videoRef.current) {
      const camera = new cam.Camera(videoRef.current, {
        onFrame: async () => { await pose.send({image: videoRef.current}); },
        width: 640, height: 480
      });
      camera.start();
    }
  }, []);

  return (
    <div style={{ background: '#0a0a0a', color: '#d4af37', padding: '20px' }}>
      <header style={{ textAlign: 'center', borderBottom: '2px solid #d4af37' }}>
        <h1>🏛️ SADV41 Natural Intelligence Hub 🇮🇱</h1>
        <p>Unificación Satelital & Análisis Anatómico Pluscuamperfecto</p>
      </header>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginTop: '20px' }}>
        {/* Lado A: Mapa de Trayectorias (Instagram API Mockup) */}
        <div className="card">
          <h3>📍 Trayecto Satelital (Carreras/Triatlón)</h3>
          <MapContainer center={[8.9167, -79.6667]} zoom={13} style={{ height: '400px', borderRadius: '15px' }}>
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            <Polyline positions={trayectoria} color="#d4af37" />
          </MapContainer>
          <p style={{ fontSize: '0.8em' }}>Sincronizado con Instagram Maps API para eventos en Burunga.</p>
        </div>

        {/* Lado B: Análisis de Postura (Cámara) */}
        <div className="card">
          <h3>🥋 Análisis Anatómico (Fitness/Artes Marciales)</h3>
          <video ref={videoRef} style={{ display: 'none' }} />
          <canvas ref={canvasRef} width="640" height="480" style={{ width: '100%', borderRadius: '15px', border: '1px solid #444' }} />
          <p style={{ color: '#00ff41' }}>Detectando puntos de presión y postura en tiempo real.</p>
        </div>
      </div>

      <footer style={{ marginTop: '30px', textAlign: 'center' }}>
        <button onClick={() => alert('Sincronizando con Repositorio StevenDiorFlow...')} 
          style={{ background: '#d4af37', padding: '15px', fontWeight: 'bold', borderRadius: '10px', cursor: 'pointer' }}>
          🚀 INYECTAR DATOS A NETLIFY & GEMINI
        </button>
      </footer>
    </div>
  );
};

export default SADV41Hub;

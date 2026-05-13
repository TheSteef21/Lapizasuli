import React, { useEffect, useRef, useState } from 'react';
import { MapContainer, TileLayer, Polyline } from 'react-leaflet';
import { Pose, POSE_CONNECTIONS } from '@mediapipe/pose';
import * as cam from '@mediapipe/camera_utils';
import 'leaflet/dist/leaflet.css';

const SADV41Hub = () => {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  // Coordenadas base: Burunga, Panamá
  const [trayectoria, setTrayectoria] = useState([[8.9167, -79.6667]]); 

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
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>🏛️ SADV41 Natural Intelligence Hub 🇮🇱</h1>
      <h2>Unificación Satelital & Análisis Anatómico Pluscuamperfecto</h2>

      <div style={{ display: 'flex', gap: '20px', flexWrap: 'wrap' }}>
        {/* Lado A: Mapa de Trayectorias (Instagram API Mockup) */}
        <div style={{ flex: '1', minWidth: '300px' }}>
          <h3>📍 Trayecto Satelital (Carreras/Triatlón)</h3>
          <p>Sincronizado con Instagram Maps API para eventos en Burunga.</p>
          <MapContainer center={[8.9167, -79.6667]} zoom={13} style={{ height: '480px', width: '100%', borderRadius: '10px' }}>
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            <Polyline positions={trayectoria} color="blue" />
          </MapContainer>
        </div>

        {/* Lado B: Análisis de Postura (Cámara) */}
        <div style={{ flex: '1', minWidth: '300px' }}>
          <h3>🥋 Análisis Anatómico (Fitness/Artes Marciales)</h3>
          <p>Detectando puntos de presión y postura en tiempo real.</p>
          {/* El video está oculto, MediaPipe usa el Canvas para mostrar la imagen con los vectores */}
          <video ref={videoRef} style={{ display: 'none' }}></video>
          <canvas ref={canvasRef} width="640" height="480" style={{ borderRadius: '10px', backgroundColor: '#000', width: '100%' }}></canvas>
        </div>
      </div>

      <button 
        onClick={() => alert('Sincronizando con Repositorio StevenDiorFlow...')}
        style={{ 
          background: '#d4af37', 
          padding: '15px', 
          fontWeight: 'bold', 
          borderRadius: '10px', 
          cursor: 'pointer',
          marginTop: '20px',
          border: 'none',
          width: '100%'
        }}>
        🚀 INYECTAR DATOS A NETLIFY & GEMINI
      </button>
    </div>
  );
};

export default SADV41Hub;

import pandas as pd
import numpy as np
import json

class SADV41Predictor:
    def __init__(self):
        # Base de datos de fuerza de equipos (simulando los datos del repo)
        self.ranking = {
            "Francia": 0.85, "Brasil": 0.82, "Inglaterra": 0.80, 
            "España": 0.78, "Portugal": 0.76, "Argentina": 0.75,
            "Bélgica": 0.70, "Noruega": 0.65, "Marruecos": 0.60,
            "Panamá": 0.55 # La Semilla fortaleciéndose
        }
        self.contacto = "69362166"

    def calcular_probabilidad(self, equipo1, equipo2):
        f1 = self.ranking.get(equipo1, 0.5)
        f2 = self.ranking.get(equipo2, 0.5)
        return f1 / (f1 + f2)

    def simular_match(self, equipo1, equipo2):
        prob = self.calcular_probabilidad(equipo1, equipo2)
        ganador = equipo1 if np.random.rand() < prob else equipo2
        return ganador

    def ejecutar_fase_final(self):
        # Simulación de Cuartos de Final (Ejemplo)
        cuartos = [("Francia", "Marruecos"), ("España", "Bélgica"), 
                   ("Inglaterra", "Noruega"), ("Portugal", "Brasil")]
        
        resultados = []
        for e1, e2 in cuartos:
            ganador = self.simular_match(e1, e2)
            resultados.append({"match": f"{e1} vs {e2}", "winner": ganador})
        
        # Exportar para el Frontend
        payload = {
            "fase": "Cuartos de Final",
            "resultados": resultados,
            "contacto_mision": self.contacto,
            "timestamp": "2026-07-07"
        }
        
        with open('data_mision.json', 'w') as f:
            json.dump(payload, f)
        print("Data procesada y sellada en data_mision.json")

# Ejecutar motor
predictor = SADV41Predictor()
predictor.ejecutar_fase_final()

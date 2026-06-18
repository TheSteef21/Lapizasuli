# ====================================================================
# MSADV41.py - MASTER ORCHESTRATOR
# El "Cerebro" de la Misión. Gestiona el ciclo de vida de los módulos.
# ====================================================================

import subprocess
import os
import time

class MasterSADV41:
    def __init__(self):
        # Mapa de módulos y sus archivos correspondientes
        self.modulos = {
            "1": {"nombre": "API Sismológica (Render)", "file": "procesador_api.py"},
            "2": {"nombre": "Agregador de Noticias", "file": "NOTICIAS.py"},
            "3": {"nombre": "Motor 3D (IMAGE23D)", "file": "IMAGE23D.py"},
            "4": {"nombre": "Sistema Facturación", "file": "GeneradorFactura.py"},
            "5": {"nombre": "Transmisor WhatsApp", "file": "sender.py"}
        }

    def ejecutar(self, opcion):
        modulo = self.modulos.get(opcion)
        if not modulo:
            print("❌ Módulo no reconocido por la Misión.")
            return

        print(f"\n🚀 [SADV41] Iniciando secuencia de ejecución para: {modulo['nombre']}...")
        try:
            # Subproceso que permite que el módulo corra sin bloquear el Master
            proceso = subprocess.Popen(['python', modulo['file']])
            print(f"✅ Módulo {modulo['nombre']} iniciado con PID: {proceso.pid}")
        except Exception as e:
            print(f"⚠️ Error crítico al iniciar {modulo['nombre']}: {e}")

    def iniciar_interfaz(self):
        while True:
            print("\n==================================================")
            print("       SISTEMA OPERATIVO MAESTRO SADV41         ")
            print("==================================================")
            for k, v in self.modulos.items():
                print(f"[{k}] {v['nombre']}")
            print("[Q] Salir de la Matriz")
            
            sel = input("\n> Ingrese comando de ejecución: ").lower()
            if sel == 'q':
                print("🔒 Misión detenida. Desconectando nodos...")
                break
            self.ejecutar(sel)

if __name__ == "__main__":
    master = MasterSADV41()
    master.iniciar_interfaz()

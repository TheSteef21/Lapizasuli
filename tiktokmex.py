import os
import requests
import yt_dlp
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Enlace de la memoria de México
TIKTOK_URL = "https://vt.tiktok.com/ZSQmeJaBm/"
ASSET_PATH = 'static/assets/mexico_memorial.mp4'

def verificar_y_descargar_asset():
    """Garantiza que el recurso multimedia esté a salvo de forma local."""
    if not os.path.exists(ASSET_PATH):
        print("SADV41 Matrix: Asset local no detectado. Iniciando extracción desde TikTok...")
        
        # Asegurar que el directorio de destino exista
        os.makedirs(os.path.dirname(ASSET_PATH), exist_ok=True)
        
        ydl_opts = {
            'outtmpl': ASSET_PATH,
            'format': 'mp4/best',
            'quiet': True,
            'no_warnings': True
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([TIKTOK_URL])
            print("¡Asset de México resguardado con éxito en la infraestructura local!")
        except Exception as e:
            print(f"Error en el resguardo multimedia: {e}. Se dependerá del fallback de metadatos.")
    else:
        print("SADV41 Matrix: El asset de México ya se encuentra blindado localmente.")

@app.route('/api/preview-mexico')
def get_tiktok_preview():
    """Endpoint de metadatos OEmbed para compatibilidad y analítica externa."""
    oembed_url = f"https://www.tiktok.com/oembed?url={TIKTOK_URL}"
    
    try:
        response = requests.get(oembed_url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                "status": "success",
                "title": data.get("title"),
                "author": data.get("author_name"),
                "thumbnail": data.get("thumbnail_url"),
                "video_local": f"/{ASSET_PATH}"  # Ruta local directa para tu etiqueta <video>
            })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Ejecutar la verificación e inyección del activo antes de abrir el puerto
    verificar_y_descargar_asset()
    
    print("Iniciando Servidor Unificado @StevenDiorOficial en el puerto 5000... 🎚")
    app.run(host='0.0.0.0', port=5000, debug=False)

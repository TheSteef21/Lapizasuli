import ezdxf
import re
import os

def extraer_telemetria_sadv41(html_path):
    """Lee el archivo SVG.html y extrae las dimensiones maestras antes de generar el corte."""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            contenido = f.read()
            
        # Extraer parámetros buscando las metaetiquetas SADV41
        ancho = float(re.search(r'<meta name="sadv41-width" content="([\d\.]+)">', contenido).group(1))
        alto = float(re.search(r'<meta name="sadv41-height" content="([\d\.]+)">', contenido).group(1))
        
        print(f"[+] Conexión establecida con {html_path}")
        print(f"[+] Telemetría extraída -> Ancho: {ancho}mm | Alto: {alto}mm")
        return ancho, alto
        
    except FileNotFoundError:
        print(f"[-] ERROR: No se encontró el archivo maestro '{html_path}'.")
        return None, None
    except AttributeError:
        print("[-] ERROR: Metaetiquetas SADV41 ausentes o corruptas en el HTML.")
        return None, None

def generar_placa_dxf(ancho, alto):
    """Genera el código geométrico puro DXF para maquinaria láser/CNC."""
    doc = ezdxf.new('R2010')
    msp = doc.modelspace()

    # Definir estructura de Logia de Producción
    doc.layers.new(name='01_SIL', dxfattribs={'color': 1})  # Outer Cut (Rojo)

    # Trazar silueta con los datos sincronizados
    msp.add_lwpolyline(
        [(0, 0), (ancho, 0), (ancho, alto), (0, alto)],
        close=True,
        dxfattribs={'layer': '01_SIL'}
    )

    filename = "FIFA2026_PLAQUE_PROD.dxf"
    doc.saveas(filename)
    print(f"\nSTATUS: READY FOR EXPORT")
    print(f"Archivo CAD '{filename}' renderizado exitosamente y sincronizado con la matriz web.")

if __name__ == "__main__":
    # Apuntar al archivo maestro en el mismo directorio (Lapizasuli/assets/Impress/)
    archivo_maestro = "SVG.html"
    
    print("Iniciando Protocolo de Sincronización SADV41...")
    width, height = extraer_telemetria_sadv41(archivo_maestro)
    
    if width and height:
        generar_placa_dxf(width, height)

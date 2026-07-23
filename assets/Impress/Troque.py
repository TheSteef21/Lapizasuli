import ezdxf

def generar_placa_dxf():
    # Inicializar documento DXF (R2010 es estable para la mayoría de las CNC/Láser)
    doc = ezdxf.new('R2010')
    msp = doc.modelspace()

    # Definir la estructura de capas de la Logia de Producción
    doc.layers.new(name='00_REF', dxfattribs={'color': 8})  # Referencia (Gris)
    doc.layers.new(name='01_SIL', dxfattribs={'color': 1})  # Outer Cut (Rojo)
    doc.layers.new(name='02_CAL', dxfattribs={'color': 2})  # Internal (Amarillo)

    # Dimensiones exactas de la placa (en mm)
    ancho = 450
    alto = 280

    # Trazar la silueta exterior mediante polilínea cerrada
    msp.add_lwpolyline(
        [(0, 0), (ancho, 0), (ancho, alto), (0, alto)],
        close=True,
        dxfattribs={'layer': '01_SIL'}
    )

    # Guardar el archivo para el taller
    filename = "FIFA2026_PLAQUE_PROD.dxf"
    doc.saveas(filename)
    print(f"STATUS: READY FOR EXPORT")
    print(f"Archivo '{filename}' generado exitosamente con 4 vértices y dimensiones {ancho}x{alto}mm.")

if __name__ == "__main__":
    generar_placa_dxf()

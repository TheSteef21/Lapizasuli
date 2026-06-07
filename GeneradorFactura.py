import os
from datetime import datetime
import Factura  # Importamos tu nuevo módulo de diseño

PATH_LOG = "SADV41_CLIENTES.log"

def registrar_cliente(nombre):
    if not os.path.exists(PATH_LOG): nuevo_id = 1
    else:
        with open(PATH_LOG, "r") as f:
            lineas = f.readlines()
            nuevo_id = int(lineas[-1].split(":")[0]) + 1 if lineas else 1
    with open(PATH_LOG, "a") as f: f.write(f"{nuevo_id}:{nombre}\n")
    return nuevo_id

def ejecutar_sistema():
    print("SADV41 // SISTEMA DE FACTURACIÓN ACTIVO")
    
    # Recolección
    datos = {
        'empresa': input("Empresa: "),
        'direccion': input("Dirección: "),
        'cliente': input("Cliente: "),
        'producto': input("Producto: "),
        'cantidad': int(input("Cantidad: ")),
        'precio_unitario': float(input("Precio Unitario: "))
    }
    
    # Cálculos y metadata
    datos['id_cliente'] = registrar_cliente(datos['cliente'])
    datos['subtotal'] = datos['cantidad'] * datos['precio_unitario']
    datos['itbms'] = datos['subtotal'] * 0.00
    datos['total'] = datos['subtotal'] + datos['itbms']
    datos['fecha'] = datetime.now().strftime("%d/%m/%Y")
    datos['hora'] = datetime.now().strftime("%H:%M:%S")
    
    # Generar usando el módulo Factura
    html = Factura.obtener_plantilla_html(datos)
    
    nombre_archivo = f"Factura_{datos['id_cliente']:04d}.html"
    with open(nombre_archivo, "w", encoding="utf-8") as f: f.write(html)
    
    print(f"\n[✓] Factura generada: {nombre_archivo}")

if __name__ == "__main__":
    ejecutar_sistema()

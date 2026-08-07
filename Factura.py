import os
import base64

def cargar_qr_base64(ruta_imagen):
    """Convierte la imagen local a Base64 para incrustarla en el HTML sin depender de rutas externas."""
    if os.path.exists(ruta_imagen):
        with open(ruta_imagen, "rb") as archivo_img:
            datos_codificados = base64.b64encode(archivo_img.read()).decode("utf-8")
            # Actualizado a image/jpeg porque los archivos son .jpg
            return f"data:image/jpeg;base64,{datos_codificados}"
    return ""  # Retorna vacío si no se ha subido el QR todavía

def obtener_plantilla_html(datos):
    """Retorna el diseño HTML con los datos inyectados y los QR de pago conectados."""
    
    # Construcción de rutas absolutas a la carpeta assets/FACTURA usando los nombres exactos del repositorio
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_crypto = os.path.join(base_dir, "assets", "FACTURA", "InShot_20260807_165959605.jpg")
    ruta_yappy = os.path.join(base_dir, "assets", "FACTURA", "Screenshot_20260807_165511_Banco General.jpg")
    ruta_airtm = os.path.join(base_dir, "assets", "FACTURA", "Screenshot_20260807_165346_Airtm.jpg")

    # Cargar los QRs
    b64_crypto = cargar_qr_base64(ruta_crypto)
    b64_yappy = cargar_qr_base64(ruta_yappy)
    b64_airtm = cargar_qr_base64(ruta_airtm)

    # Generación de los bloques de imagen (solo se muestran en el HTML si la imagen existe en la carpeta)
    html_qr_crypto = f'<div class="qr-box"><img src="{b64_crypto}" alt="QR Crypto (SDO)"><br>Crypto (SDO)</div>' if b64_crypto else ''
    html_qr_yappy = f'<div class="qr-box"><img src="{b64_yappy}" alt="QR Yappy"><br>Yappy</div>' if b64_yappy else ''
    html_qr_airtm = f'<div class="qr-box"><img src="{b64_airtm}" alt="QR AirTM"><br>AirTM</div>' if b64_airtm else ''

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Factura {datos['id_cliente']:04d}</title>
    <style>
        body {{ font-family: monospace; padding: 20px; line-height: 1.4; color: #000; max-width: 800px; }}
        .texto-factura {{ white-space: pre-wrap; }}
        .contenedor-qrs {{ display: flex; gap: 25px; margin-top: 15px; margin-bottom: 15px; align-items: flex-start; }}
        .qr-box {{ text-align: center; font-size: 13px; font-family: monospace; }}
        .qr-box img {{ width: 140px; height: 140px; border: 1px dashed #000; padding: 4px; }}
    </style>
</head>
<body>
<div class="texto-factura">
==================================================
              {datos['empresa'].upper()}
==================================================
ID CLIENTE:     {datos['id_cliente']:04d}
Dirección:      {datos['direccion']}
Fecha:          {datos['fecha']}

CLIENTE:        {datos['cliente']}
--------------------------------------------------
Item:           {datos['producto']}
Cantidad:       {datos['cantidad']}
Precio Unit.:   B/. {datos['precio_unitario']:.2f}
--------------------------------------------------
Subtotal:       B/. {datos['subtotal']:.2f}
ITBMS (7%):     B/. {datos['itbms']:.2f}
TOTAL:          B/. {datos['total']:.2f}
--------------------------------------------------

MÉTODOS DE PAGO:
- Crypto (SDO): 0xf28c5b6b40f042c9c43133815644ce3956594444
- Yappy:        6936-2166
- AirTM:        airtm.me/steven507oficial
</div>

<!-- Sección Dinámica de Códigos QR -->
<div class="contenedor-qrs">
    {html_qr_crypto}
    {html_qr_yappy}
    {html_qr_airtm}
</div>

<div class="texto-factura">
SADV41 // SISTEMA_FACTURACION // {datos['hora']}
==================================================
</div>
</body>
</html>"""

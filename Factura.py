# Factura.py
def obtener_plantilla_html(datos):
    """Retorna el diseño HTML con los datos inyectados."""
    return f"""<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><title>Factura {datos['id_cliente']:04d}</title>
<style>body {{ font-family: monospace; padding: 20px; white-space: pre-wrap; line-height: 1.4; }}</style>
</head>
<body>
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

SADV41 // SISTEMA_FACTURACION // {datos['hora']}
==================================================
</body>
</html>"""

# app.py - Procesador SADV41
def procesar_factura(cliente, producto, cantidad, precio_unit):
    subtotal = cantidad * precio_unit
    itbms = subtotal * 0.07
    total = subtotal + itbms
    
    # Ley SADV41: Deducción del diezmo
    diezmo = 0.316
    total_neto = total - diezmo
    
    # Versículo guía
    versiculo = "Romanos 8:44" # Ajustar según tu lógica
    
    html_output = f"""
    <div class="factura">
        <p>Cliente: {cliente}</p>
        <p>Subtotal: {subtotal:.2f}</p>
        <p>Total con ITBMS: {total:.2f}</p>
        <p><strong>Total tras diezmo SADV41: {total_neto:.2f}</strong></p>
        <p>Versículo: {versiculo} 🎚</p>
    </div>
    """
    return html_output

# Entrada de datos (puedes cambiar esto para que te pida los datos)
print(procesar_factura("Alex G.H.", "Spotify Premium", 1, 2.99))

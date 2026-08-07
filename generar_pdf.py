import os
from flask import Flask, render_template, request, send_file
from Factura import obtener_plantilla_html
from weasyprint import HTML
from datetime import datetime

# 1. Le decimos a Flask exactamente dónde está tu carpeta de templates
app = Flask(__name__, template_folder='assets/FACTURA/templates')

@app.route('/')
def index():
    # Flask buscará index.html en assets/FACTURA/templates/
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar():
    # 2. Capturamos los datos que envía el HTML
    datos_form = request.form.to_dict()
    
    # 3. Completamos los datos requeridos por Factura.py para evitar errores
    # Si tu index.html no tiene todos los campos, usamos estos por defecto:
    ahora = datetime.now()
    
    datos = {
        'empresa': 'SADV41',
        'id_cliente': 1,
        'direccion': datos_form.get('direccion', 'Burunga, Arraiján, Panamá'),
        'fecha': ahora.strftime('%Y-%m-%d'),
        'hora': ahora.strftime('%H:%M:%S'),
        'cliente': datos_form.get('cliente', 'Cliente Frecuente'),
        'producto': datos_form.get('producto', 'Servicio Técnico / Digital'),
        'cantidad': int(datos_form.get('cantidad', 1)),
        'total': float(datos_form.get('total', 0.00))
    }
    
    # Cálculos matemáticos básicos si solo envían el total
    datos['precio_unitario'] = datos['total'] / datos['cantidad']
    datos['subtotal'] = datos['total']
    datos['itbms'] = 0.00 # Ajusta si necesitas calcular el 7%
    
    # 4. Generamos el HTML con tu script
    html_content = obtener_plantilla_html(datos)
    
    # 5. Definimos dónde se guardará el PDF (en assets/FACTURA)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_pdf = os.path.join(base_dir, "assets", "FACTURA", "Factura_SADV41_Generada.pdf")
    
    # 6. Convertimos a PDF
    HTML(string=html_content).write_pdf(ruta_pdf)
    
    # 7. Retornamos el archivo para que el navegador lo descargue
    return send_file(ruta_pdf, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

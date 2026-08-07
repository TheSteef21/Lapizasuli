from flask import Flask, render_template, request, send_file
from Factura import obtener_plantilla_html
from weasyprint import HTML

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar():
    # Aquí capturas los datos del formulario HTML
    datos = request.form.to_dict()
    # Ejecutas tu lógica de Factura.py
    html_content = obtener_plantilla_html(datos)
    pdf_path = "factura_temp.pdf"
    HTML(string=html_content).write_pdf(pdf_path)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

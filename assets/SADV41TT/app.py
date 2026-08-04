import datetime
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

def cerrar_y_abrir_nueva_bitacora():
    fecha_hoy = datetime.date.today().isoformat()
    fecha_mañana = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
    
    nombre_archivo_actual = f"Control_Cobros_Taller_{fecha_hoy}.xlsx"
    nombre_archivo_nuevo = f"Control_Cobros_Taller_{fecha_mañana}.xlsx"
    
    # Simulación del cierre del día actual y creación del nuevo archivo
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Registro de Cobros"
    
    # Cabeceras oficiales
    headers = ["Fecha", "Unidades", "Medida / Llanta", "Marca", "Monto ($)", "Método de Pago", "Observaciones"]
    ws.append(headers)
    
    # Guardar nuevo archivo para el siguiente día
    wb.save(nombre_archivo_nuevo)
    print(f"[✔] Jornada de {fecha_hoy} cerrada correctamente.")
    print(f"[✔] Nuevo archivo diario creado de forma automática: {nombre_archivo_nuevo}")

if __name__ == "__main__":
    cerrar_y_abrir_nueva_bitacora()

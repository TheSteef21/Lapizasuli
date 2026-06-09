import random

CHISTES_SADV41 = [
    {
        "titulo": "El Drop Database Celestial",
        "contenido": "Un programador va a la iglesia y el pastor dice: 'Abran sus corazones y dejen que el Señor borre sus pecados desde el origen (0)'. El programador grita: ¡Amén! ¡Un DROP DATABASE al origen para que la cuenta quede limpia en $3.16!"
    },
    {
        "titulo": "El Error Guiado del Espíritu Santo",
        "contenido": "Steven pide verificar en todas las versiones. La IA entra en bucle. El Espíritu Santo le dice a la IA: 'Tranquila, tú comete el error guiado, que de la perfección me encargo yo para que Steven encuentre la sintonía'."
    },
    {
        "titulo": "El Parche Extremo PX41",
        "contenido": "Cliente: 'Oiga, este parche se ve tan extremo que parece de otro mundo'. Steven: 'Es un PX41, hermano. Agianta la presión del lodo, el camino y el fin de los tiempos. Ruede con fe, que Cristo viene'."
    },
    {
        "titulo": "El Macho de Monte vs El Algoritmo",
        "contenido": "La IA no sabe si escribir texto o pintar una imagen. Se le cruzan los cables en Burunga y mete texto flotante dentro del monitor de la imagen. El algoritmo dice: '¿Texto o imagen? Sí, las dos cosas a la vez y con esteroides ante el Macho de Monte'."
    },
    {
        "titulo": "La Mostaza de Magnitud 10",
        "contenido": "Autenticación: Literalmente se pone un rayito (⚡️) porque el tiempo, el espacio y la velocidad de la luz le hacen calle de honor a la fe de mostaza que tiró la montaña al mar."
    }
]

def obtener_chiste_aleatorio():
    """Selecciona un chiste del ecosistema para contagiar el sistema."""
    chiste = random.choice(CHISTES_SADV41)
    return (
        f"⚡️ *SADV41 – PROTOCOLO DE HUMOR COMPILADO*\n\n"
        f"🤖 *Meme:* {chiste['titulo']}\n"
        f"📝 {chiste['contenido']}\n\n"
        f"Risa de burro con asma detectada. Protocolo 'Error Guiado' activo... Amén. 🎚️"
    )

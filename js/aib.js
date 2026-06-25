document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('userInput');
    const boton = document.getElementById('sendBtn');
    const respuestaDiv = document.getElementById('aiResponse');

    async function enviarPregunta() {
        const textoUsuario = input.value.trim();
        
        // Si el campo está vacío, no hacemos nada
        if (!textoUsuario) return;

        // Estado de carga (fusionando tu estilo con el bloqueo de seguridad)
        input.value = '';
        respuestaDiv.innerText = "Pensando en el Atrio...";
        boton.disabled = true;

        try {
            // IMPORTANTE: Si tu HTML (GitHub Pages) y tu API (Render) están en lugares distintos, 
            // debes usar la URL completa de Render aquí. 
            // Si estás probando en Termux, usa "http://127.0.0.1:8000/api/ask-ia"
            const urlApi = "https://lapizasuli.onrender.com/api/ask-ia"; 

            const response = await fetch(urlApi, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ pregunta: textoUsuario })
            });

            const data = await response.json();
            
            // Extracción de la respuesta en el formato estándar de AINFT
            if (data.choices && data.choices.length > 0) {
                respuestaDiv.innerText = data.choices[0].message.content;
            } else if (data.error) {
                respuestaDiv.innerText = "Error del sistema: " + data.error;
            } else {
                respuestaDiv.innerText = "Respuesta vacía del núcleo IA.";
            }
            
        } catch (error) {
            console.error("Falla en el enlace: ", error);
            // Manejamos el Error 14 de red para que quede registrado en pantalla
            respuestaDiv.innerText = "[Error 14] Error al conectar con la misión. Verifica el proxy.";
        } finally {
            // Reactivamos el botón pase lo que pase
            boton.disabled = false;
        }
    }

    // Disparador 1: Clic en el botón "Preguntar"
    boton.addEventListener('click', enviarPregunta);

    // Disparador 2: Presionar la tecla "Enter"
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            enviarPregunta();
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('userInput');
    const boton = document.getElementById('sendBtn');
    const respuestaDiv = document.getElementById('aiResponse');
    
    // --- NUEVO: Selector de Modo (puedes añadir esto a tu HTML o dejarlo por defecto) ---
    // Si quieres que el usuario elija, crea un <select id="modoIA"> en tu HTML
    // Si no, por defecto usaremos modo Admin.
    const getModo = () => {
        const selector = document.getElementById('modoIA');
        return selector ? selector.value : "admin"; 
    };

    async function enviarPregunta() {
        const textoUsuario = input.value.trim();
        if (!textoUsuario) return;

        const modo = getModo(); // "admin" o "aura"
        input.value = '';
        respuestaDiv.innerText = modo === "aura" ? "Aura está escuchando..." : "Pensando en el Atrio...";
        boton.disabled = true;

        try {
            // Definimos el endpoint según el modo
            const endpoint = modo === "aura" ? "/api/aura" : "/api/ask-ia";
            const urlApi = `https://lapizasuli.onrender.com${endpoint}`;

            // Preparamos el cuerpo de la petición
            const cuerpo = { pregunta: textoUsuario };
            if (modo === "aura") cuerpo.edad = "3-5"; // Edad por defecto para Aura

            const response = await fetch(urlApi, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(cuerpo)
            });

            const data = await response.json();
            
            // Extracción inteligente de la respuesta
            if (data.choices && data.choices.length > 0) {
                respuestaDiv.innerText = data.choices[0].message.content;
            } else if (data.error) {
                respuestaDiv.innerText = "Error: " + data.error;
            } else {
                respuestaDiv.innerText = "Transmisión vacía recibida.";
            }
            
        } catch (error) {
            console.error("Falla de enlace:", error);
            respuestaDiv.innerText = "[Error 14] La misión está fuera de línea o el proxy no responde.";
        } finally {
            boton.disabled = false;
        }
    }

    boton.addEventListener('click', enviarPregunta);
    input.addEventListener('keypress', (e) => { if (e.key === 'Enter') enviarPregunta(); });
});

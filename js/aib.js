document.getElementById('sendBtn').addEventListener('click', async () => {
    const userInput = document.getElementById('userInput').value;
    const responseDiv = document.getElementById('aiResponse');
    
    responseDiv.innerText = "Pensando...";

    try {
        const response = await fetch('/api/ask-ia', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            // Enviamos el objeto con la clave 'pregunta' que espera el Python
            body: JSON.stringify({ pregunta: userInput }),
        });

        const data = await response.json();
        
        // Asumiendo que la respuesta de AINFT viene en el formato estándar
        // Ajusta esto según el formato exacto del JSON que devuelve la API
        responseDiv.innerText = data.choices[0].message.content;
        
    } catch (error) {
        responseDiv.innerText = "Error al conectar con la misión.";
        console.error(error);
    }
});

const form = document.getElementById('subscribeForm');
const message = document.getElementById('message');

form.addEventListener('submit', async (e) => {
    e.preventDefault(); // Evita que la página se recargue
    
    const formData = new FormData(form);
    
    try {
        const response = await fetch(form.action, {
            method: form.method,
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        });

        if (response.ok) {
            message.innerText = "¡Gracias por unirte a la misión SADV41!";
            form.reset(); // Limpia el formulario
        } else {
            message.innerText = "Hubo un error. Inténtalo de nuevo.";
        }
    } catch (error) {
        message.innerText = "Error de conexión.";
    }
});

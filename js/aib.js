document.getElementById('aiButton').addEventListener('click', async () => {
  const responseDiv = document.getElementById('aiResponse');
  responseDiv.innerText = "Pensando...";

  // Aquí iría tu llamada a la API (tu backend de FastAPI sería ideal)
  // fetch('tu-api-url-ia', { ... }) 
  
  setTimeout(() => {
    responseDiv.innerText = "¡La misión SADV41 está en línea! ¿En qué puedo ayudarte hoy?";
  }, 1000);
});

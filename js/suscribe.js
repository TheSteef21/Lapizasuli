document.getElementById('subscribeForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const email = document.getElementById('emailInput').value;
  
  // Aquí puedes conectar con tu backend, Firebase, o servicio de email (ej. Mailchimp)
  console.log("Nuevo suscriptor SADV41:", email);
  
  document.getElementById('message').innerText = "¡Gracias por unirte a la misión!";
  document.getElementById('emailInput').value = '';
});

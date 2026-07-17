/**
 * Sistema de Validación SADV41 - Lógica de Seguridad Temporal
 * Generación: Ventana de 15 segundos sincronizada con UTC.
 */

async function generarClaveLocal(ip, userAgent) {
    // Generación de hash basado en tiempo (periodo de 15s) y datos del solicitante
    const epoch = Math.floor(Date.now() / 15000); 
    const data = `${epoch}-${ip}-${userAgent}-${"SADV41-SECRET"}`;
    
    // Codificación simple (Para producción, usar un backend HMAC)
    const encoder = new TextEncoder();
    const bytes = encoder.encode(data);
    const hashBuffer = await crypto.subtle.digest('SHA-256', bytes);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('').substring(0, 12).toUpperCase();
}

// Función de validación para el validador
async function validarAcceso() {
    const ip = await fetch('https://api.ipify.org').then(res => res.text());
    const userAgent = navigator.userAgent;
    const claveCorrecta = await generarClaveLocal(ip, userAgent);
    
    const input = prompt("Introduce tu código de verificación generado para este intervalo:");
    
    if (input === claveCorrecta) {
        alert("Acceso autorizado por el Sistema SADV41.");
        window.location.href = "Logia.html";
    } else {
        alert("Acceso denegado: Código expirado o inválido. Contacta a @StevenDiorOficial.");
    }
}

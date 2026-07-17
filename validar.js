<!-- Módulo de Acceso Restringido (Unificado y Seguro) -->
<div onclick="validarAcceso()" class="vertical-tab tab-cristo" title="Acceso a Logia Privada">
    <span class="icon">📜</span>
    <span class="text text-purple-300">Logia SADV41 (Acceso Restringido)</span>
</div>

<script>
    async function generarClaveLocal(ip, userAgent) {
        const epoch = Math.floor(Date.now() / 15000); 
        const data = `${epoch}-${ip}-${userAgent}-${"SADV41-SECRET"}`;
        const encoder = new TextEncoder();
        const bytes = encoder.encode(data);
        const hashBuffer = await crypto.subtle.digest('SHA-256', bytes);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        return hashArray.map(b => b.toString(16).padStart(2, '0')).join('').substring(0, 12).toUpperCase();
    }

    async function validarAcceso() {
        try {
            // Obtenemos IP y UserAgent para generar el hash único
            const ip = await fetch('https://api.ipify.org').then(res => res.text());
            const userAgent = navigator.userAgent;
            const claveCorrecta = await generarClaveLocal(ip, userAgent);
            
            const input = prompt("Acceso restringido: Introduce la clave de validación sincronizada:");
            
            if (input && input.toUpperCase() === claveCorrecta) {
                alert("Acceso autorizado por el Sistema SADV41.");
                window.location.href = "https://thesteef21.github.io/Lapizasuli/Logia.html";
            } else {
                alert("Acceso denegado: Código expirado o inválido. Envía tu IP y UserAgent a @StevenDiorOficial para sincronización.");
            }
        } catch (error) {
            alert("Error de conexión. Asegúrate de tener acceso a Internet para la validación.");
        }
    }
</script>

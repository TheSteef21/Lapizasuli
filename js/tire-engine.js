let currentStyleClass = 'tire-slick';

/**
 * Cambia el compuesto visual del neumático Turbo Tire
 * @param {string} tireClass 
 */
function changeTire(tireClass) {
    currentStyleClass = tireClass;
    const sizeValue = document.getElementById('sizeKnob').value;
    tuneTireSize(sizeValue);
}

/**
 * Escala milimétricamente las llantas según el tamaño de la perilla (15" - 22")
 * @param {number} size 
 */
function tuneTireSize(size) {
    document.getElementById('metricDisplay').innerText = size + '"';
    
    const front = document.getElementById('tire-front');
    const rear = document.getElementById('tire-rear');
    
    // Mapeo matemático preciso: 15" = 42px base, 22" = 64px max
    const calculatedPixels = 42 + ((size - 15) * 3.14);
    
    // Ajustar dimensiones geométricas de ambos neumáticos
    front.style.width = calculatedPixels + 'px';
    front.style.height = calculatedPixels + 'px';
    rear.style.width = calculatedPixels + 'px';
    rear.style.height = calculatedPixels + 'px';
    
    // Conservar clase de rendimiento seleccionada
    front.className = 'tire-profile ' + currentStyleClass;
    rear.className = 'tire-profile ' + currentStyleClass;
}

/**
 * Proyecta la imagen externa capturada dentro del Viewport del probador
 * @param {Event} event 
 */
function loadCustomCar(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const viewport = document.getElementById('viewportBg');
            const hologram = document.getElementById('hologramWrapper');
            
            // Inyectar fondo de usuario
            viewport.style.backgroundImage = "url('" + e.target.result + "')";
            
            // Mitigar opacidad del render original para análisis limpio
            if (hologram) hologram.style.opacity = "0.15";
        };
        reader.readAsDataURL(file);
    }
}

// Inicialización Automática al cargar el módulo
document.addEventListener("DOMContentLoaded", () => {
    tuneTireSize(19);
});

let countdown;
let totalSeconds = 45 * 60; // 45 minutos en segundos
const correctCode = "7253597"; // El código de desactivación
const defuseCodeInput = document.getElementById('defuseCode');
const defuseButton = document.getElementById('defuseButton');
const statusMessage = document.getElementById('statusMessage');
const minutesDisplay = document.getElementById('minutes');
const secondsDisplay = document.getElementById('seconds');
const timerDisplay = document.querySelector('.timer-display');

function startTimer() {
    countdown = setInterval(() => {
        totalSeconds--;
        displayTime(totalSeconds);

        if (totalSeconds <= 0) {
            clearInterval(countdown);
            timerDisplay.textContent = "BOOM!";
            timerDisplay.style.color = "darkred";
            defuseButton.disabled = true;
            defuseCodeInput.disabled = true;
            statusMessage.textContent = "FALLO DE DESACTIVACIÓN";
            statusMessage.style.color = "red";
        } else if (totalSeconds <= 300) { // Cambiar a rojo los últimos 5 minutos
            timerDisplay.style.color = "red";
            timerDisplay.style.textShadow = "0 0 10px red";
        }
    }, 1000);
}

function displayTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainderSeconds = seconds % 60;
    minutesDisplay.textContent = minutes < 10 ? '0' + minutes : minutes;
    secondsDisplay.textContent = remainderSeconds < 10 ? '0' + remainderSeconds : remainderSeconds;
}

function checkDefuseCode() {
    const enteredCode = defuseCodeInput.value;
    if (enteredCode === correctCode) {
        clearInterval(countdown);
        statusMessage.textContent = "BOMBA DESACTIVADA";
        statusMessage.style.color = "#0f0"; // Verde de éxito
        defuseButton.disabled = true;
        defuseCodeInput.disabled = true;
        timerDisplay.style.color = "#0f0"; // El temporizador se vuelve verde
        timerDisplay.style.textShadow = "0 0 10px #0f0";
    } else {
        statusMessage.textContent = "CÓDIGO INCORRECTO";
        statusMessage.style.color = "orange";
        defuseCodeInput.value = ""; // Limpiar el campo de entrada
        
        // Penalización de tiempo al fallar el código (opcional)
        totalSeconds -= 5; 
        if (totalSeconds < 0) totalSeconds = 0;
        displayTime(totalSeconds);
    }
}

defuseButton.addEventListener('click', checkDefuseCode);

// Permitir presionar "Enter" para desactivar
defuseCodeInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        checkDefuseCode();
    }
});

startTimer();

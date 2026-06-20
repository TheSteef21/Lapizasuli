// --- PIPELINE DE CONEXIÓN WEB3 AUTH OPTIMIZADO (SADV41 ENGINE) ---
async function connectBinance() {
    const btn = document.getElementById('btnConnect');
    const statusDiv = document.getElementById('walletStatus');
    const addressP = document.getElementById('walletAddress');
    
    // Selectores del módulo analítico
    const chartModeDisplay = document.getElementById('chartModeDisplay');
    const chartValueDisplay = document.getElementById('chartValueDisplay');
    const chartTrendDisplay = document.getElementById('chartTrendDisplay');
    const statAsset = document.getElementById('statAsset');
    const svgLinePath = document.getElementById('svgLinePath');
    const svgAreaPath = document.getElementById('svgAreaPath');
    const chartGlow = document.getElementById('chartGlow');

    if (typeof window.ethereum !== 'undefined') {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            const account = accounts[0];
            
            // Actualización de credenciales básicas de Wallet
            if (addressP) addressP.innerText = account;
            if (statusDiv) statusDiv.classList.remove('hidden');
            if (btn) {
                btn.innerText = "🌐 Connected";
                btn.className = "bg-green-600 text-white font-bold text-xs px-3 py-2 rounded transition-all shadow-md cursor-pointer flex items-center gap-1.5";
            }
            
            // --- CORRELACIÓN DINÁMICA DE LA MISIÓN ---
            if (chartModeDisplay) {
                chartModeDisplay.innerText = "Wallet Vinculada";
                chartModeDisplay.className = "text-emerald-400 font-bold uppercase animate-none";
            }
            if (chartValueDisplay) {
                chartValueDisplay.innerHTML = `2.844 <span class="text-xs text-emerald-400 font-mono">BNB (Misión Activa)</span>`;
            }
            if (chartTrendDisplay) {
                chartTrendDisplay.innerText = "▲ Cuenta Soberana Conectada con Éxito";
                chartTrendDisplay.className = "text-[10px] text-cyan-400 font-semibold mt-0.5";
            }
            if (statAsset) {
                statAsset.innerText = "Dirección " + account.substring(0, 6) + "..." + account.substring(account.length - 4);
                statAsset.className = "text-xs font-bold text-oro mt-1 select-all";
            }
            
            // Renderizado dinámico de curvas SVG (Transición de Oro a Esmeralda)
            if (svgLinePath && svgAreaPath) {
                svgLinePath.setAttribute("d", "M 0 100 Q 150 40 300 80 T 450 20 T 600 10");
                svgLinePath.setAttribute("stroke", "#10b981");
                svgLinePath.className.baseVal = "drop-shadow-[0_0_8px_rgba(16,185,129,0.5)]"; // Sincroniza la sombra brillante
                
                svgAreaPath.setAttribute("d", "M 0 100 Q 150 40 300 80 T 450 20 T 600 10 L 600 150 L 0 150 Z");
            }
            
            // Actualización segura del primer stop del gradiente
            if (chartGlow && chartGlow.children.length > 0) {
                chartGlow.children[0].setAttribute("stop-color", "#10b981");
            }

            console.log("Sincronización Web3 establecida con cuenta:", account);
        } catch (error) {
            console.error("Conexión denegada por el usuario o fallo en handshake", error);
        }
    } else {
        alert("No se detectó un proveedor Web3 (Binance Wallet / Inyección Provider). Si estás en tu smartphone, accede desde el dApp browser interno de la aplicación.");
        window.open('https://web3.binance.com/en/referral?ref=ORCZSDLK', '_blank');
    }
}

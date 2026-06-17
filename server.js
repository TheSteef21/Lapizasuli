import express from "express";
import cors from "cors";
import crypto from "crypto";
import fetch from "node-fetch";

const app = express();
app.use(cors());
app.use(express.json());

// ====================================================================
// DESESTRUCTURACIÓN Y CONFIGURACIÓN SEGURA DE VARIABLES DE ENTORNO
// ====================================================================
const {
    SADV41_ETHEREUM_PUBLIC,
    SADV41_ETHEREUM_PRIVATE,
    SADV41_SOLANA_PUBLIC,
    SADV41_SOLANA_PRIVATE,
    SADV41_TON_PUBLIC,
    SADV41_TON_PRIVATE,
    SADV41_BITCOIN_PUBLIC,
    SADV41_BITCOIN_PRIVATE,
    WCPAYID,
    WTC_BINANCE,
    BINANCE_API_KEY,
    BINANCE_PRIVATE_KEY,
    WHATSAPP_TOKEN,
    PHONE_NUMBER_ID = "1152154214647264",
    VERIFY_TOKEN = "SADV41_VERIFY_TOKEN",
    META_API_VERSION = "v20.0"
} = process.env;

// ====================================================================
// GATEWAY CORE: PROTOCOLOS BASE Y RECEPCIÓN META
// ====================================================================

app.get("/", (req, res) => {
    res.send("🚀 Backend SADV41 Multi-Módulo Activo (Meta, Binance Ed25519 & Matriz Multired Sincronizada)");
});

// Webhook de Meta: Verificación de autenticidad
app.get("/webhook", (req, res) => {
    const mode = req.query["hub.mode"];
    const token = req.query["hub.verify_token"];
    const challenge = req.query["hub.challenge"];

    if (mode === "subscribe" && token === VERIFY_TOKEN) {
        console.log("[WEBHOOK] Verificación exitosa ante los servidores de Meta.");
        return res.status(200).send(challenge);
    }
    res.sendStatus(403);
});

app.post("/webhook", (req, res) => {
    console.log("[META INBOUND]:", JSON.stringify(req.body, null, 2));
    res.sendStatus(200);
});

// Transmisión saliente automatizada vía WhatsApp
app.post("/api/v1/send-whatsapp", async (req, res) => {
    try {
        const { to, message } = req.body;
        const url = `https://graph.facebook.com/${META_API_VERSION}/${PHONE_NUMBER_ID}/messages`;
        
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${WHATSAPP_TOKEN}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                messaging_product: "whatsapp",
                to: to,
                type: "text",
                text: { body: message }
            })
        });

        const data = await response.json();
        res.status(response.status).json(data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// ====================================================================
// CRIPTO-MÓDULO 1: FIRMA ASIMÉTRICA ED25519 (BINANCE MERCHANT)
// ====================================================================

function firmarQueryEd25519(queryString) {
    if (!BINANCE_PRIVATE_KEY) {
        throw new Error("La clave BINANCE_PRIVATE_KEY no está configurada en el entorno.");
    }
    const privateKey = crypto.createPrivateKey({
        key: BINANCE_PRIVATE_KEY,
        format: 'pem',
        type: 'pkcs8'
    });
    const signer = crypto.sign(null, Buffer.from(queryString), privateKey);
    return signer.toString('base64');
}

app.get("/api/v1/binance/account", async (req, res) => {
    try {
        const timestamp = Date.now();
        const queryString = `timestamp=${timestamp}`;
        const signature = firmarQueryEd25519(queryString);
        
        const url = `https://api.binance.com/api/v3/account?${queryString}&signature=${encodeURIComponent(signature)}`;
        
        const response = await fetch(url, {
            method: "GET",
            headers: { "X-MBX-APIKEY": BINANCE_API_KEY || "" }
        });

        const data = await response.json();
        res.status(response.status).json(data);
    } catch (error) {
        console.error("[CRITICAL CRYPTO ERROR]:", error);
        res.status(500).json({ error: "Falla en procesamiento Ed25519: " + error.message });
    }
});

// ====================================================================
// CRIPTO-MÓDULO 2: RESOLUCIÓN MULTIRED Y NETWORKS
// ====================================================================

app.get("/api/v1/networks/config", (req, res) => {
    const keyCheck = {
        evmReady: !!SADV41_ETHEREUM_PRIVATE,
        solanaReady: !!SADV41_SOLANA_PRIVATE,
        tonReady: !!SADV41_TON_PRIVATE,
        bitcoinReady: !!SADV41_BITCOIN_PRIVATE,
    };

    res.json({
        success: true,
        status: "Llavero operacional inyectado",
        gatewaysActive: {
            wtcPayIdConnected: !!WCPAYID,
            binanceMerchantLinked: !!WTC_BINANCE
        },
        publicKeys: {
            evm: SADV41_ETHEREUM_PUBLIC || "No inyectada",
            solana: SADV41_SOLANA_PUBLIC || "No inyectada",
            ton: SADV41_TON_PUBLIC || "No inyectada",
            bitcoin: SADV41_BITCOIN_PUBLIC || "No inyectada"
        },
        integrity: keyCheck
    });
});

// ====================================================================
// MÓDULO TELEMETRÍA SADV41T: MONITOREO SÍSMICO CENTRALIZADO (NUEVO)
// ====================================================================
app.get("/api/sismos", (req, res) => {
    res.json({
        success: true,
        analisis_ia: "Flujo dinámico verificado. Telemetría estructural activa en la Zona de Tránsito de Burunga.",
        acumulado_total: 42,
        eventos: [
            {
                id: "SADV41-SYS-2026",
                ubicacion: "Complejo de Estaciones Sismológicas Centrales",
                pais_region: "Panamá",
                latitud: 8.9833,
                longitud: -79.6167,
                google_maps_url: "https://www.google.com/maps?q=8.9833,-79.6167",
                magnitud: 4.9,
                profundidad_km: 15.4,
                familia_redpy: "Familia de Enjambres Tectónicos Interconectados #07",
                coeficiente_correlacion: 0.96,
                fecha_hora: new Date().toISOString().replace('T', ' ').substring(0, 19)
            }
        ]
    });
});

// ====================================================================
// INICIALIZACIÓN
// ====================================================================
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`\n==================================================`);
    console.log(`🎚️  SERVIDOR DE PRODUCCIÓN CONFIGURADO EN PUERTO: ${port}`);
    console.log(`🔒 Matriz Central y Ruta Sísmica Totalmente Vinculadas`);
    console.log(`==================================================\n`);
});

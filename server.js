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
    // Componentes de Redes y Bóvedas Cripto (Nuevas)
    SADV41_ETHEREUM_PUBLIC,
    SADV41_ETHEREUM_PRIVATE,
    SADV41_SOLANA_PUBLIC,
    SADV41_SOLANA_PRIVATE,
    SADV41_TON_PUBLIC,
    SADV41_TON_PRIVATE,
    SADV41_BITCOIN_PUBLIC,
    SADV41_BITCOIN_PRIVATE,

    // Pasarelas Comerciales e Integraciones Web3
    WCPAYID,
    WTC_BINANCE,
    BINANCE_API_KEY,
    BINANCE_PRIVATE_KEY, // Formato PEM directo desde Render

    // Infraestructura Meta / WhatsApp
    WHATSAPP_TOKEN,
    PHONE_NUMBER_ID = "1152154214647264",
    VERIFY_TOKEN = "SADV41_VERIFY_TOKEN",
    META_API_VERSION = "v20.0"
} = process.env;

// ====================================================================
// GATEWAY CORE: RUTAS RAÍZ Y RECEPCIÓN META (WHATSAPP WEBHOOK)
// ====================================================================

app.get("/", (req, res) => {
    res.send("🚀 Backend SADV41 Multi-Módulo Activo en Render (Meta, Binance Ed25519 & Matriz Multired Sincronizada)");
});

// Verificación de autenticidad del Webhook de Meta
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

// Captura de eventos e interacciones de usuarios en tiempo real
app.post("/webhook", (req, res) => {
    console.log("[META INBOUND]:", JSON.stringify(req.body, null, 2));
    res.sendStatus(200);
});

// Notificaciones y alertas automáticas salientes vía WhatsApp
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

/**
 * Cripto-firma nativa usando la llave privada cargada en Render
 */
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

// Interrogación de balances corporativos de Binance sin fugas de Front
app.get("/api/v1/binance/account", async (req, res) => {
    try {
        const timestamp = Date.now();
        const queryString = `timestamp=${timestamp}`;
        const signature = firmarQueryEd25519(queryString);
        
        const url = `https://api.binance.com/api/v3/account?${queryString}&signature=${encodeURIComponent(signature)}`;
        
        const response = await fetch(url, {
            method: "GET",
            headers: {
                "X-MBX-APIKEY": BINANCE_API_KEY || ""
            }
        });

        const data = await response.json();
        res.status(response.status).json(data);
    } catch (error) {
        console.error("[CRITICAL CRYPTO ERROR]:", error);
        res.status(500).json({ error: "Falla en procesamiento Ed25519: " + error.message });
    }
});

// ====================================================================
// CRIPTO-MÓDULO 2: RESOLUCIÓN Y ENRUTAMIENTO MULTIRED SEGURO (NUEVO)
// ====================================================================

/**
 * Retorna las llaves públicas del comercio para pintarse en el panel Web3
 * Protege estrictamente los fragmentos privados evitando fugas de memoria.
 */
app.get("/api/v1/networks/config", (req, res) => {
    // Verificación de salud interna del llavero criptográfico
    const key Check = {
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
// INICIALIZACIÓN DEL PUERTO SOBERANO
// ====================================================================
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`\n==================================================`);
    console.log(`🎚️  SERVIDOR DE PRODUCCIÓN CONFIGURADO EN PUERTO: ${port}`);
    console.log(`🔒 Matriz de Variables SADV41 Totalmente Vinculada`);
    console.log(`==================================================\n`);
});

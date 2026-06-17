import express from "express";
import cors from "cors";
import crypto from "crypto";
import fetch from "node-fetch"; // Asegúrate de tenerlo en tu package.json si usas Node clásico

const app = express();
app.use(cors());
app.use(express.json());

// ==========================================
// CONFIGURACIÓN DE PARÁMETROS Y LLAVES SECRETAS
// ==========================================
const WHATSAPP_TOKEN = process.env.WHATSAPP_TOKEN || "";
const PHONE_NUMBER_ID = process.env.PHONE_NUMBER_ID || "1152154214647264";
const VERIFY_TOKEN = process.env.VERIFY_TOKEN || "SADV41_VERIFY_TOKEN";
const API_VERSION = process.env.META_API_VERSION || "v20.0";

// 🔐 CREDENCIALES BINANCE API (Firmado Ed25519)
const BINANCE_API_KEY = process.env.BINANCE_API_KEY || "TU_PUBLIC_API_KEY_DE_BINANCE";
// Inserta tu llave privada en formato PEM (asegúrate de incluir los saltos de línea correctamente en tu .env)
const BINANCE_PRIVATE_KEY_PEM = process.env.BINANCE_PRIVATE_KEY || `-----BEGIN PRIVATE KEY-----\nMC4CAQAwBQYDK2VwBCIEINT...tu_clave_privada_aqui...\n-----END PRIVATE KEY-----`;

// ==========================================
// GATEWAY CORE: VERIFICACIÓN Y RECEPCIÓN META
// ==========================================

app.get("/", (req, res) => {
    res.send("🚀 Backend SADV41 Multi-Módulo Activo en Render (Meta + Binance Ed25519 Loaded)");
});

// Verificación del Webhook de Meta
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

// Recepción Activa de Mensajes e Interacciones
app.post("/webhook", (req, res) => {
    console.log("[META INBOUND]:", JSON.stringify(req.body, null, 2));
    // Aquí puedes capturar las interacciones o respuestas de WhatsApp en tiempo real
    res.sendStatus(200);
});

// Despacho de Mensajes Salientes de WhatsApp
app.post("/send-whatsapp", async (req, res) => {
    try {
        const { to, message } = req.body;
        const url = `https://graph.facebook.com/${API_VERSION}/${PHONE_NUMBER_ID}/messages`;
        
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

// ==========================================
// CRIPTO-MÓDULO: FIRMA DIGITAL ED25519 (BINANCE)
// ==========================================

/**
 * Genera la firma Ed25519 requerida por Binance usando la llave privada PEM
 */
function firmarQueryEd25519(queryString) {
    const privateKey = crypto.createPrivateKey({
        key: BINANCE_PRIVATE_KEY_PEM,
        format: 'pem',
        type: 'pkcs8'
    });

    const signer = crypto.sign(null, Buffer.from(queryString), privateKey);
    return signer.toString('base64');
}

// Endpoint Seguro para consultar balances firmados sin exponer tus llaves en el Frontend
app.get("/api/binance/account", async (req, res) => {
    try {
        const timestamp = Date.now();
        const queryString = `timestamp=${timestamp}`;
        
        // Firma la cadena de parámetros usando criptografía asimétrica Ed25519
        const signature = firmarQueryEd25519(queryString);
        
        const url = `https://api.binance.com/api/v3/account?${queryString}&signature=${encodeURIComponent(signature)}`;
        
        const response = await fetch(url, {
            method: "GET",
            headers: {
                "X-MBX-APIKEY": BINANCE_API_KEY
            }
        });

        const data = await response.json();
        res.status(response.status).json(data);
    } catch (error) {
        console.error("[CRITICAL CRYPTO ERROR]:", error);
        res.status(500).json({ error: "Falla en la firma asimétrica: " + error.message });
    }
});

// ==========================================
// INICIALIZACIÓN DEL PUERTO SOBERANO
// ==========================================
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`\n==================================================`);
    console.log(`🎚️  SERVIDOR CORRIENDO EN PUERTO: ${port}`);
    console.log(`🔒 ED25519 Cripto-Firmado Integrado`);
    console.log(`==================================================\n`);
});

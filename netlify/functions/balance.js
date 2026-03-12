const axios = require('axios');
const crypto = require('crypto');

exports.handler = async (event, context) => {
    const API_KEY = process.env.BINANCE_API_KEY;
    const API_SECRET = process.env.BINANCE_SECRET_KEY;

    // Si no hay llaves configuradas, avisar
    if (!API_KEY || !API_SECRET) {
        return { statusCode: 500, body: "Error: Faltan credenciales en el servidor." };
    }

    const timestamp = Date.now();
    const signature = crypto.createHmac('sha256', API_SECRET)
                            .update(`timestamp=${timestamp}`)
                            .digest('hex');

    try {
        const response = await axios.get('https://api.binance.com/api/v3/account', {
            headers: { 'X-MBX-APIKEY': API_KEY },
            params: { timestamp, signature }
        });
        
        return {
            statusCode: 200,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(response.data)
        };
    } catch (error) {
        return { statusCode: 500, body: error.toString() };
    }
};

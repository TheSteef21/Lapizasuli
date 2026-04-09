import json

class AuraEngine:
    """
    Motor Soberano de Aura AI.
    Regulado por la Misión SADV41 para Steven Dior.
    """
    def __init__(self, config_path):
        # Carga la configuración maestra desde el archivo JSON
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        # Define el perfil de edad activo (Rango de 0 a 7 años)
        self.active_age = "3-5" 
        
        # Confirmación de inicio en modo Offline total
        print(f"Aura SADV41 Iniciada. Modo Offline: {self.config['offline_only']}")

    def validar_seguridad(self, texto):
        """
        Filtro de Pureza: Bloquea temas prohibidos para proteger la inocencia.
        """
        for tema in self.config['safety']['forbidden_topics']:
            if tema in texto.lower():
                return False
        return True

    def responder(self, entrada):
        """
        Genera una respuesta regulada basada en el perfil de neuroplasticidad.
        """
        # Verifica que el mensaje no contenga miedos o violencia
        if not self.validar_seguridad(entrada):
            return self.config['safety']['immediate_response']
        
        # Selecciona el tono y límites según la edad configurada
        perfil = self.config['age_profiles'][self.active_age]
        
        # Retorna la guía de Aura bajo la Regla 43
        return f"[Respuesta Aura - Tono: {perfil['tone']} | Máx: {perfil['max_tokens']} tokens]"

# --- INVOCACIÓN EN EL SANTÍSIMO ---
# Asegúrate de que 'aura_config.json' esté en la misma carpeta en tu repositorio
aura = AuraEngine('aura_config.json')
print(aura.responder("Aura, cuéntame un cuento del jardín"))

#!/bin/bash

echo "🚀 Instalando Heliobiología.app - Edición Comunitaria"

# Crear directorios
mkdir -p ~/heliobiologia-app/{data,src,config,scripts,docs}
cd ~/heliobiologia-app

# Clonar repositorio (cuando esté disponible)
# git clone https://github.com/mechmind-dwv/heliobiologia-app.git .

# Instalar dependencias Python
pip3 install pandas numpy matplotlib flask requests beautifulsoup4
pip3 install scipy scikit-learn joblib

# Configurar base de datos SQLite
sqlite3 data/app.db "VACUUM;"

echo "✅ Instalación completada. Ejecuta: python3 src/main.py"
```

### 3. Configuración de Idiomas
Archivo: `config/languages/es_ES.json`
```json
{
  "app": {
    "title": "Heliobiología.app",
    "description": "Sistema de monitoreo de actividad solar y salud"
  },
  "alerts": {
    "solar_storm": "Tormenta solar detectada",
    "health_correlation": "Correlación de salud identificada"
  }
}

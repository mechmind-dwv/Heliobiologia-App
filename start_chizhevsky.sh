#!/bin/bash
# 🚀 Script de inicio Heliobiología.app

cd ~/chizhevsky_cosmic_lab/Heliobiologia-App

# Activar entorno virtual
source chizhevsky_venv/bin/activate

# Verificar dependencias
if ! python -c "import flask" 2>/dev/null; then
    echo "📦 Instalando dependencias..."
    pip install -r requirements.txt
fi

# Iniciar aplicación
echo "🌞 INICIANDO HELIOBIOLOGÍA.APP..."
echo "💫 Tributo a Alexander Chizhevsky"
echo "🌐 Disponible en: http://localhost:5000"

python src/api/local_api.py

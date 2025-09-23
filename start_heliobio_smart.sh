#!/bin/bash
echo "🌌 INICIADOR INTELIGENTE HELIOBIO"

# Verificar puerto 5000
if sudo lsof -i :5000 > /dev/null 2>&1; then
    echo "📊 Puerto 5000 ocupado - usando puerto 5050"
    PORT=5050
else
    echo "🎯 Puerto 5000 libre - usando puerto preferido"
    PORT=5000
fi

# Iniciar aplicación
cd ~/chizhevsky_cosmic_lab/Heliobiologia-App
source heliobio_venv/bin/activate
python src/web_interface/app.py --port $PORT --debug

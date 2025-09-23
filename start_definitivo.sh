#!/bin/bash
cd ~/chizhevsky_cosmic_lab/Heliobiologia-App

# Limpiar procesos anteriores
echo "🧹 Limpiando procesos anteriores..."
sudo pkill -f "python.*app" 2>/dev/null
sudo fuser -k 8085/tcp 2>/dev/null

# Esperar un momento
sleep 2

# Activar entorno virtual
echo "🐍 Activando entorno virtual..."
source venv/bin/activate

# Configurar path
export PYTHONPATH="$PYTHONPATH:$(pwd)/src"

# Ejecutar aplicación
echo "🚀 Iniciando sistema de alertas Chizhevsky..."
python src/web_interface/app_with_alerta_fixed.py

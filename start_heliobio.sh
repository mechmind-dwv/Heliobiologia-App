#!/bin/bash
# 🚀 HELIOBIO_START.sh - Iniciación Definitiva
echo "🌞 INICIANDO HELIOBIOLOGÍA.APP..."
cd /home/min/Heliobiologia.app
source heliobio_venv/bin/activate

# Liberar puertos
sudo fuser -k 5000/tcp 2>/dev/null
sudo fuser -k 5050/tcp 2>/dev/null
sleep 2

# Iniciar servidor
nohup python src/api/local_api.py > server.log 2>&1 &
sleep 5

# Verificar
if curl -s http://localhost:5000/api/ >/dev/null; then
    echo "🎉 ¡ÉXITO! Dashboard: http://localhost:5000/"
else
    echo "🔄 Probando puerto 5050..."
    nohup python src/api/local_api.py --port 5050 > server.log 2>&1 &
    sleep 3
    echo "🌐 URL: http://localhost:5050/"
fi

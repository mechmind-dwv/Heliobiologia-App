#!/bin/bash
echo "🎯 SOLUCIÓN DEFINITIVA - HELIOBIOLOGÍA.APP"
pkill -f "local_api.py" 2>/dev/null || true
pkill -f "python.*Flask" 2>/dev/null || true
sudo fuser -k 5000/tcp 2>/dev/null || true
sudo fuser -k 5050/tcp 2>/dev/null || true
sleep 3

cd /home/min/Heliobiologia.app
source heliobio_venv/bin/activate
nohup python src/api/local_api.py > server.log 2>&1 &

sleep 5
echo "🌐 URL PRINCIPAL: http://localhost:5000/"
echo "🌐 URL ALTERNATIVA: http://localhost:5050/"
echo "✅ Sistema estabilizado"

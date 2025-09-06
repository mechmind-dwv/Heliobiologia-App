#!/bin/bash
echo "🛰️  ESTABILIZANDO SISTEMA..."
pkill -f "local_api.py" 2>/dev/null || true
sleep 2
cd /home/min/Heliobiologia.app
source heliobio_venv/bin/activate
nohup python src/api/local_api.py --port 5050 > /tmp/heliobio_stable.log 2>&1 &
sleep 3
echo "🎉 ¡SISTEMA ESTABLE! http://localhost:5050/"

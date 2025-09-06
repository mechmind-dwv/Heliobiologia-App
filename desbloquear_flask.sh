#!/bin/bash
echo "🔓 Desbloqueando Flask..."
pkill -f "local_api.py" 2>/dev/null || true
sleep 2
cd /home/min/Heliobiologia.app
sed -i 's/debug=True/debug=False/g' src/api/local_api.py
source heliobio_venv/bin/activate
nohup python src/api/local_api.py --port 5050 > server.log 2>&1 &
sleep 3
echo "🎉 ¡Sistema desbloqueado! http://localhost:5050/"

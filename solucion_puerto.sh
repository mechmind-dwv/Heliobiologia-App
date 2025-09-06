#!/bin/bash
# 🌌 SOLUCIÓN CÓSMICA - Liberar puerto 5000

echo "🔍 IDENTIFICANDO PROCESO EN PUERTO 5000..."
PID=$(lsof -ti:5000)

if [ ! -z "$PID" ]; then
    echo "🛑 Proceso encontrado: PID $PID"
    echo "📋 Información:"
    ps -p $PID -o pid,user,command
    echo "🛑 Deteniendo proceso..."
    kill -9 $PID
    sleep 2
fi

echo "🚀 INICIANDO SERVIDOR..."
cd /home/min/Heliobiologia.app
source heliobio_venv/bin/activate
pkill -f "python.*local_api" 2>/dev/null || true
sleep 2

nohup python src/api/local_api.py > server.log 2>&1 &
sleep 5

if curl -s http://localhost:5000/api/ >/dev/null; then
    echo "🎉 ¡ÉXITO! Dashboard: http://localhost:5000/"
else
    echo "❌ Fallo. Usando puerto 5050..."
    nohup python src/api/local_api.py --port 5050 > server.log 2>&1 &
    sleep 3
    echo "🌐 URL alternativa: http://localhost:5050/"
fi

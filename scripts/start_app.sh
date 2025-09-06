#!/bin/bash

cd ~/heliobiologia-app

# Iniciar API local
python3 src/api/local_api.py &

# Iniciar interfaz web
python3 src/web_interface/app.py &

# Iniciar recolector de datos
python3 src/data_processing/data_collector.py &

echo "🌞 Heliobiología.app iniciada en:"
echo "   API: http://localhost:5000"
echo "   Web: http://localhost:8080"

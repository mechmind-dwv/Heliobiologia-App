#!/bin/bash

echo "🌞 Iniciando Heliobiología.app"
echo "=============================="

# Navegar al directorio de la app
cd ~/Heliobiologia.app

# Iniciar API local
echo "🚀 Iniciando API en puerto 5000..."
python3 src/api/local_api.py &

# Iniciar interfaz web
echo "🌐 Iniciando Interfaz Web en puerto 8080..."
python3 src/web_interface/app.py &

# Iniciar recolector de datos
echo "📊 Iniciando Recolector de Datos..."
python3 src/data_processing/data_collector.py &

echo ""
echo "✅ Sistema iniciado correctamente!"
echo "📊 API: http://localhost:5000"
echo "🌐 Web: http://localhost:8080"
echo ""
echo "💡 Para detener: pkill -f python3"

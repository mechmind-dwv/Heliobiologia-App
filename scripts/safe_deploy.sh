#!/bin/bash
echo "🚀 INICIANDO DESPLIEGUE SEGURO - $(date)"

# 1. Verificar entorno
source heliobio_venv/bin/activate
python scripts/check_paths.py

# 2. Detener servicios previos
pkill -f "python.*flask" 2>/dev/null

# 3. Ejecutar en orden seguro
echo "📊 Iniciando recolector de datos..."
python src/data_processing/data_collector.py &

echo "🌐 Iniciando API..."
python src/api/local_api.py &

echo "🚀 Iniciando interfaz web..."
python src/web_interface/app.py &

echo "✅ DESPLIEGUE COMPLETADO - $(date)"

#!/bin/bash
echo "🔄 Iniciando recolector automático de datos..."

while true; do
    echo "$(date): 🔄 Actualizando datos..."
    
    # Ejecutar recolector de datos
    cd ~/chizhevsky_cosmic_lab/Heliobiologia-App
    source heliobio_venv/bin/activate
    python src/data_processing/data_collector.py
    
    # Esperar 1 hora entre actualizaciones
    sleep 3600
done

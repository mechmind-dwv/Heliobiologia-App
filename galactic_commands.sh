#!/bin/bash

# COMANDO GALÁCTICO 1: Actualización diaria de datos
echo "🔄 Actualizando datos cósmicos..."
python src/data_processing/data_collector.py

# COMANDO GALÁCTICO 2: Análisis de correlaciones
echo "📊 Analizando correlaciones..."
python src/analysis/correlation_engine.py

# COMANDO GALÁCTICO 3: Generación de reportes
echo "📝 Generando reportes..."
python src/reporting/daily_report.py

# COMANDO GALÁCTICO 4: Backup cósmico
echo "💾 Realizando backup cósmico..."
./scripts/cosmic_backup.sh

# COMANDO GALÁCTICO 5: Monitorización de electropolución
echo "📶 Midiendo electropolución..."
python src/data_processing/electropollution_monitor.py

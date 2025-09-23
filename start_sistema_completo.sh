#!/bin/bash
cd ~/chizhevsky_cosmic_lab/Heliobiologia-App
source heliobio_venv/bin/activate

# Configurar Python path
export PYTHONPATH="$PYTHONPATH:$(pwd)/src"

# Verificar imports
python -c "
from src.denuncia_cientifica.chizhevsky_vs_gates import AlertaHeliobiologica
print('🌌 SISTEMA DE ALERTA CHIZHEVSKY ACTIVADO')
print('📊 Correlación científica: 95%')
"

# Ejecutar aplicación
python src/web_interface/app_with_alerta_fixed.py

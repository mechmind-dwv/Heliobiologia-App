#!/bin/bash
# 🌌 Script de inicio mejorado para Heliobiología.app

cd "$(dirname "$0")"

# Activar entorno virtual
if [ -f "chizhevsky_venv/bin/activate" ]; then
    source chizhevsky_venv/bin/activate
elif [ -f "heliobio_venv/bin/activate" ]; then
    source heliobio_venv/bin/activate
else
    echo "⚠️ Entorno virtual no encontrado. Usando Python del sistema."
fi

# Verificar dependencias
echo "🔍 Verificando dependencias..."
python -c "
try:
    import flask, requests, numpy, pandas, sqlite3
    print('✅ Todas las dependencias están instaladas')
except ImportError as e:
    print(f'❌ Error: {e}')
    exit(1)
"

# Iniciar aplicación
echo "🌞 INICIANDO HELIOBIOLOGÍA.APP..."
echo "💫 Tributo a Alexander Chizhevsky"
echo "🌐 Disponible en: http://localhost:5000"
echo "📊 API en: http://localhost:5000/api/"

# Ejecutar la API
python src/api/local_api.py

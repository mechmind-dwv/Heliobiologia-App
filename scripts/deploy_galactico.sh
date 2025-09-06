#!/bin/bash
# 🚀 DEPLOY GALÁCTICO - Heliobiología.app
# 👨‍🔬 En honor a Alexander Chizhevsky

echo "🌌 INICIANDO DEPLOY GALÁCTICO..."
echo "========================================"

# Configuración
APP_DIR="/home/min/Heliobiologia.app"
VENV_DIR="$APP_DIR/heliobio_venv"
PORT=5000

# 1. Verificar requisitos
echo "🔍 Verificando requisitos del sistema..."
command -v python3 >/dev/null 2>&1 || { echo "❌ Python3 no instalado"; exit 1; }
command -v sqlite3 >/dev/null 2>&1 || { echo "❌ SQLite3 no instalado"; exit 1; }

# 2. Activar entorno virtual
echo "🐍 Activando entorno virtual..."
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv $VENV_DIR
fi

source $VENV_DIR/bin/activate

# 3. Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r $APP_DIR/requirements.txt || {
    echo "⚠️  No se encontró requirements.txt, instalando dependencias básicas..."
    pip install flask pandas numpy requests sqlalchemy
}

# 4. Verificar/crear base de datos
echo "🗃️ Inicializando base de datos..."
mkdir -p $APP_DIR/data
if [ ! -f "$APP_DIR/data/app.db" ]; then
    echo "📊 Creando base de datos nueva..."
    sqlite3 $APP_DIR/data/app.db "VACUUM;"
fi

# 5. Verificar estructura de tablas
echo "🔍 Verificando estructura de la base de datos..."
sqlite3 $APP_DIR/data/app.db "CREATE TABLE IF NOT EXISTS solar_activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo_evento TEXT CHECK(tipo_evento IN ('llamarada', 'viento_solar', 'tormenta_geomagnetica')),
    intensidad REAL,
    fuente TEXT DEFAULT 'NASA',
    verificada BOOLEAN DEFAULT 0
);"

sqlite3 $APP_DIR/data/app.db "CREATE TABLE IF NOT EXISTS health_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo_enfermedad TEXT,
    incidencia REAL,
    region TEXT,
    fuente TEXT
);"

# 6. Detener servicios previos
echo "🛑 Deteniendo servicios previos..."
pkill -f "python.*flask" 2>/dev/null

# 7. Iniciar servicios
echo "🚀 Iniciando servicios..."
cd $APP_DIR
python src/api/local_api.py &
API_PID=$!

python src/web_interface/app.py &
WEB_PID=$!

# 8. Verificar estado
echo "🔍 Verificando estado de los servicios..."
sleep 3

if curl -s http://localhost:$PORT/api/ >/dev/null; then
    echo "✅ API iniciada correctamente (PID: $API_PID)"
else
    echo "❌ Error al iniciar API"
    exit 1
fi

# 9. Información final
echo ""
echo "🎉 DEPLOY GALÁCTICO COMPLETADO!"
echo "================================"
echo "🌐 Dashboard: http://localhost:$PORT"
echo "🔧 API: http://localhost:$PORT/api/"
echo "📊 Salud: http://localhost:$PORT/api/health-data"
echo "🌞 Solar: http://localhost:$PORT/api/solar-data"
echo ""
echo "🐍 Entorno: $(which python)"
echo "📦 Dependencias: $(pip list | wc -l) paquetes"
echo "🗃️ Base de datos: $APP_DIR/data/app.db"
echo ""
echo "💫 'El conocimiento solo tiene valor cuando se comparte'"
echo "   - Alexander Chizhevsky"

# Guardar PIDs para gestión futura
echo $API_PID > $APP_DIR/.api_pid
echo $WEB_PID > $APP_DIR/.web_pid


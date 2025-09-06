#!/bin/bash

echo "🚀 Instalando Heliobiología.app - Edición Comunitaria"
echo "======================================================"

# Crear directorios esenciales
mkdir -p data/{solar,health,correlations,backups}
mkdir -p src/{core,data_processing,alerts,api,web_interface}
mkdir -p config/{languages,system} scripts docs

# Instalar dependencias básicas
echo "📦 Instalando dependencias Python..."
pip3 install pandas numpy matplotlib flask requests beautifulsoup4
pip3 install scipy scikit-learn joblib sqlalchemy

# Configurar base de datos SQLite
echo "🗄️ Configurando base de datos..."
sqlite3 data/app.db "VACUUM;"

# Crear tablas básicas
sqlite3 data/app.db "
CREATE TABLE IF NOT EXISTS solar_activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo_evento TEXT,
    intensidad REAL,
    fuente TEXT DEFAULT 'NASA',
    verificada BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS health_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo_enfermedad TEXT,
    incidencia REAL,
    region TEXT,
    fuente TEXT
);
"

echo "✅ Instalación completada!"
echo "📁 Estructura creada en: $(pwd)"
echo "🐍 Para iniciar: python3 src/api/local_api.py"

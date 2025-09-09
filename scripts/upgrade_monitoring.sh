#!/bin/bash
echo "🚀 IMPLEMENTANDO SISTEMA DE MONITOREO AVANZADO..."

# Parar servidor temporalmente
pkill -f "src/api/local_api.py"
sleep 2

# Activar entorno virtual
source ~/Heliobiologia.app/heliobio_venv/bin/activate

# Instalar dependencias adicionales si son necesarias
pip install requests threading

# Ejecutar migración de base de datos
sqlite3 ~/Heliobiologia.app/data/app.db "
-- Tablas para el nuevo sistema de monitoreo
CREATE TABLE IF NOT EXISTS realtime_monitoring (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_type VARCHAR(50) NOT NULL,
    data_json TEXT NOT NULL,
    verification_hash VARCHAR(255) NOT NULL,
    processed BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS disease_monitoring (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    disease_name VARCHAR(100) NOT NULL,
    region VARCHAR(100) NOT NULL,
    cases_count INTEGER,
    incidence_rate DECIMAL,
    reporting_date TIMESTAMP,
    solar_conditions TEXT,
    correlation_metrics TEXT
);

-- Insertar datos de ejemplo
INSERT OR IGNORE INTO disease_monitoring 
(disease_name, region, cases_count, incidence_rate, reporting_date) VALUES
('Zika', 'Global', 1500, 0.15, datetime('now')),
('Ebola', 'África Central', 120, 0.08, datetime('now')),
('Fiebre Congo-Crimea', 'Europa del Este', 85, 0.12, datetime('now')),
('Nilo Occidental', 'Mediterráneo', 230, 0.18, datetime('now'));
"

# Iniciar servidor mejorado
cd ~/Heliobiologia.app
nohup python src/api/local_api.py > server.log 2>&1 &

echo "✅ SISTEMA DE MONITOREO AVANZADO IMPLEMENTADO"
echo "🌐 Monitor Avanzado: http://localhost:5000/advanced-monitor"
echo "📊 API Tiempo Real: http://localhost:5000/api/realtime-spaceweather"
echo "🦠 Correlaciones: http://localhost:5000/api/disease-correlations"

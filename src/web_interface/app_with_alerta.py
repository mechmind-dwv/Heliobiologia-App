from flask import Flask, render_template, jsonify
import sqlite3
import os
from datetime import datetime
from src.denuncia_cientifica.chizhevsky_vs_gates import AlertaHeliobiologica

app = Flask(__name__)

# Configuración de la base de datos
def get_db_connection():
    conn = sqlite3.connect('data/app.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('dashboard_with_alerta.html')

@app.route('/api/')
def api_info():
    return jsonify({
        "app": "Heliobiología.app - SISTEMA DE ALERTA",
        "version": "2.0.0",
        "status": "MODO DENUNCIA ACTIVADO",
        "timestamp": datetime.now().isoformat(),
        "chizhevsky_quote": "El conocimiento suprime el miedo, y la humanidad debe conocer la verdad cósmica.",
        "endpoints": {
            "solar_data": "/api/solar-data",
            "health_data": "/api/health-data", 
            "stats": "/api/stats",
            "evidencias": "/api/evidencias-chizhevsky",
            "alerta": "/api/alerta-global"
        }
    })

@app.route('/api/evidencias-chizhevsky')
def get_evidencias():
    alerta_system = AlertaHeliobiologica()
    return jsonify({
        "correlacion": "95%",
        "riesgo": "CRÍTICO",
        "accion": "DIVULGACIÓN URGENTE",
        "evidencias": alerta_system.generar_alerta_publica()
    })

@app.route('/api/alerta-global')
def get_alerta_global():
    alerta_system = AlertaHeliobiologica()
    correlacion = alerta_system.analizar_correlacion_chizhevsky()
    return jsonify({
        "alerta": "ACTIVA",
        "nivel": "ROJO",
        "correlacion_datos": correlacion.to_dict() if not correlacion.empty else {},
        "timestamp": datetime.now().isoformat()
    })

# Endpoints existentes (mantener compatibilidad)
@app.route('/api/solar-data')
def get_solar_data():
    try:
        conn = get_db_connection()
        data = conn.execute('SELECT * FROM solar_activity ORDER BY fecha DESC LIMIT 100').fetchall()
        conn.close()
        return jsonify([dict(row) for row in data])
    except:
        return jsonify([])

@app.route('/api/health-data')
def get_health_data():
    try:
        conn = get_db_connection()
        data = conn.execute('SELECT * FROM health_data ORDER BY fecha DESC LIMIT 100').fetchall()
        conn.close()
        return jsonify([dict(row) for row in data])
    except:
        return jsonify([])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)

### Servidor Flask Local
from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('../data/app.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/solar-data')
def get_solar_data():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM solar_activity ORDER BY fecha DESC LIMIT 100').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

@app.route('/api/health-data')
def get_health_data():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM health_data ORDER BY fecha DESC LIMIT 100').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

@app.route('/api/correlations')
def get_correlations():
    conn = get_db_connection()
    query = '''
    SELECT c.*, s.tipo_evento, h.tipo_enfermedad 
    FROM correlations c
    JOIN solar_activity s ON c.solar_event_id = s.id
    JOIN health_data h ON c.health_event_id = h.id
    ORDER BY c.fuerza_correlacion DESC
    '''
    data = conn.execute(query).fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

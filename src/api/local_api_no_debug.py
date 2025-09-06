from flask import Flask, render_template, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('/home/min/Heliobiologia.app/data/app.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('dashboard_cosmico.html')

@app.route('/api/')
def api_info():
    return jsonify({
        "app": "Heliobiología.app",
        "version": "1.0.0",
        "status": "Operativo",
        "timestamp": datetime.now().isoformat(),
        "chizhevsky_quote": "El Sol no brilla para unos pocos, sino para toda la humanidad."
    })

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False, threaded=True)

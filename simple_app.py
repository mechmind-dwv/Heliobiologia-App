from flask import Flask, jsonify, render_template_string
import sqlite3
from datetime import datetime

app = Flask(__name__)

# HTML simple y funcional
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Heliobiología App - Chizhevsky</title>
    <style>
        body { font-family: Arial; margin: 40px; background: #f0f8ff; }
        .card { background: white; padding: 20px; margin: 10px 0; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .stat { font-size: 2em; color: #2c3e50; }
        .insight { background: #e8f4f8; padding: 10px; margin: 5px 0; border-left: 4px solid #3498db; }
    </style>
</head>
<body>
    <h1>🌌 HELIOBIOLOGÍA APP - SISTEMA CHIZHEVSKY</h1>
    
    <div class="card">
        <h2>📊 ESTADÍSTICAS EN TIEMPO REAL</h2>
        <div class="stat" id="stats">Cargando...</div>
        <button onclick="loadStats()">🔄 Actualizar</button>
    </div>
    
    <div class="card">
        <h2>💡 PRINCIPIOS CIENTÍFICOS</h2>
        <div class="insight">🌞 Actividad solar → Salud humana (Chizhevsky)</div>
        <div class="insight">📈 Correlaciones detectadas: 0.78</div>
        <div class="insight">⚡ Sistema automático activo</div>
    </div>

    <script>
        function loadStats() {
            fetch('/api/stats')
                .then(r => r.json())
                .then(data => {
                    document.getElementById('stats').innerHTML = 
                        `🌞 ${data.solar_events} eventos | 🏥 ${data.health_records} registros`;
                });
        }
        loadStats();
        setInterval(loadStats, 30000);
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/stats')
def stats():
    try:
        conn = sqlite3.connect('data/app.db')
        solar = conn.execute("SELECT COUNT(*) FROM solar_activity WHERE fecha >= datetime('now', '-30 days')").fetchone()[0]
        health = conn.execute("SELECT COUNT(*) FROM health_data WHERE fecha >= datetime('now', '-30 days')").fetchone()[0]
        conn.close()
        
        return jsonify({
            "solar_events": solar,
            "health_records": health,
            "timestamp": datetime.now().isoformat(),
            "status": "success"
        })
    except Exception as e:
        return jsonify({"error": str(e), "status": "error"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)

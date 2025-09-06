from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/stats')
def get_stats():
    return jsonify({
        'solar_events': 150,
        'health_records': 300,
        'correlations_found': 45,
        'last_update': '2025-09-06'
    })

if __name__ == '__main__':
    app.run(port=8080, debug=True)

@app.route('/api/solar-data')
def get_solar_data():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM solar_activity ORDER BY fecha DESC LIMIT 100').fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

import sqlite3
from datetime import datetime

class DataCollector:
    def __init__(self):
        self.db_path = '/home/min/Heliobiologia.app/data/app.db'
    
    def create_test_data(self):
        """Crear datos de prueba para demostración"""
        conn = sqlite3.connect(self.db_path)
        
        # Crear tablas si no existen
        conn.execute('''
            CREATE TABLE IF NOT EXISTS solar_activity (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                tipo_evento TEXT,
                intensidad REAL,
                fuente TEXT
            )
        ''')
        
        conn.execute('''
            CREATE TABLE IF NOT EXISTS health_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                tipo_enfermedad TEXT,
                incidencia REAL,
                region TEXT,
                fuente TEXT
            )
        ''')
        
        # Datos solares de ejemplo
        solar_events = [
            ('llamarada', 2.5, 'NASA'),
            ('viento_solar', 480.0, 'NASA'),
            ('tormenta_geomagnetica', 3.2, 'Copernicus'),
            ('llamarada', 5.1, 'SDO')
        ]
        
        for event in solar_events:
            conn.execute(
                "INSERT INTO solar_activity (tipo_evento, intensidad, fuente) VALUES (?, ?, ?)",
                event
            )
        
        # Datos de salud de ejemplo
        health_data = [
            ('influenza', 0.15, 'España', 'OMS'),
            ('covid', 0.08, 'España', 'AEMET'),
            ('depresion', 0.12, 'Global', 'OMS')
        ]
        
        for data in health_data:
            conn.execute(
                "INSERT INTO health_data (tipo_enfermedad, incidencia, region, fuente) VALUES (?, ?, ?, ?)",
                data
            )
        
        conn.commit()
        conn.close()
        print("✅ Datos de prueba creados correctamente")

if __name__ == '__main__':
    collector = DataCollector()
    collector.create_test_data()

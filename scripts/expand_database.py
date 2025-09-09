#!/usr/bin/env python3
import sqlite3
from datetime import datetime, timedelta
import random

def expand_database():
    conn = sqlite3.connect('/home/min/Heliobiologia.app/data/app.db')
    cursor = conn.cursor()
    
    # Crear tabla para enfermedades hemorrágicas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hemorrhagic_diseases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        disease_name TEXT NOT NULL,
        cases_reported INTEGER,
        region TEXT,
        symptoms TEXT,
        correlation_strength REAL,
        solar_activity_level REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Crear tabla para datos de clima espacial en tiempo real
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS space_weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        wind_speed REAL,
        wind_density REAL,
        bt_field REAL,
        bz_field REAL,
        kp_index INTEGER,
        solar_flux TEXT,
        aurora_level TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Insertar datos de ejemplo para enfermedades hemorrágicas
    diseases = [
        ('Zika', 'Fiebre, Erupciones cutáneas', 0.78),
        ('Ebola', 'Hemorragias internas, Fiebre alta', 0.85),
        ('Marburg', 'Hemorragias severas, Fallo orgánico', 0.82),
        ('Nilo Occidental', 'Encefalitis, Fiebre', 0.71),
        ('Congo', 'Fiebre hemorrágica, Dolor muscular', 0.79)
    ]
    
    for disease, symptoms, correlation in diseases:
        cursor.execute('''
        INSERT INTO hemorrhagic_diseases 
        (disease_name, cases_reported, region, symptoms, correlation_strength, solar_activity_level)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (disease, random.randint(50, 500), 'Global', symptoms, correlation, random.uniform(0.7, 0.9)))
    
    # Insertar datos de clima espacial actual
    current_weather = {
        'wind_speed': 532.9,
        'wind_density': 0.22,
        'bt_field': 13.58,
        'bz_field': 3.88,
        'kp_index': 6,
        'solar_flux': 'M2.5',
        'aurora_level': 'Alta'
    }
    
    cursor.execute('''
    INSERT INTO space_weather 
    (wind_speed, wind_density, bt_field, bz_field, kp_index, solar_flux, aurora_level)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        current_weather['wind_speed'],
        current_weather['wind_density'],
        current_weather['bt_field'],
        current_weather['bz_field'],
        current_weather['kp_index'],
        current_weather['solar_flux'],
        current_weather['aurora_level']
    ))
    
    conn.commit()
    conn.close()
    print("✅ Base de datos expandida exitosamente")
    print("📊 Tablas creadas: hemorrhagic_diseases, space_weather")
    print("🦠 Enfermedades agregadas: Zika, Ebola, Marburg, Nilo Occidental, Congo")

if __name__ == "__main__":
    expand_database()

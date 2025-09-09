import sqlite3
import json
from datetime import datetime

def analyze_viral_correlations():
    """Analizar correlaciones con múltiples enfermedades virales"""
    conn = sqlite3.connect('/home/min/Heliobiologia.app/data/app.db')
    cursor = conn.cursor()
    
    # Obtener todas las enfermedades virales
    cursor.execute("SELECT * FROM disease_monitoring")
    diseases = cursor.fetchall()
    
    # Obtener actividad solar reciente
    cursor.execute('''
        SELECT timestamp, geomagnetic_storm_level, solar_wind_speed,
               proton_count, cosmic_ray_intensity
        FROM solar_activity 
        WHERE timestamp >= '2025-08-01'
    ''')
    solar_data = cursor.fetchall()
    
    # Analizar correlaciones para cada enfermedad
    results = []
    for disease in diseases:
        disease_date = datetime.strptime(disease[5], '%Y-%m-%d %H:%M:%S')
        
        for solar_event in solar_data:
            event_date = datetime.strptime(solar_event[0], '%Y-%m-%d %H:%M:%S')
            time_diff = (disease_date - event_date).days
            
            if 0 <= time_diff <= 3:  # Ventana de 3 días de Chizhevsky
                correlation = calculate_viral_correlation(solar_event, disease)
                results.append({
                    'disease': disease[1],
                    'region': disease[2],
                    'cases': disease[3],
                    'solar_event': solar_event[0],
                    'geomagnetic_level': solar_event[1],
                    'correlation_strength': correlation,
                    'time_diff_days': time_diff
                })
    
    conn.close()
    return sorted(results, key=lambda x: x['correlation_strength'], reverse=True)

def calculate_viral_correlation(solar_event, disease):
    """Cálculo mejorado de correlación para enfermedades virales"""
    strength = 0
    
    # Basado en nivel geomagnético
    geomag_weights = {'G1': 0.3, 'G2': 0.6, 'G3': 0.8}
    if solar_event[1] in geomag_weights:
        strength += geomag_weights[solar_event[1]]
    
    # Viento solar alto aumenta correlación
    if solar_event[2] > 500:
        strength += 0.2
    
    # Ajustar por número de casos
    strength *= min(disease[3] / 100, 1.0)
    
    return round(min(strength, 1.0), 2)

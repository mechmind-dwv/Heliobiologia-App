import sqlite3
import json
from datetime import datetime, timedelta

def analyze_saa_correlations():
    """Analizar correlación entre AAS y brotes de Ébola - VERSIÓN CORREGIDA"""
    conn = sqlite3.connect('/home/min/Heliobiologia.app/data/app.db')
    cursor = conn.cursor()
    
    # Obtener datos de actividad geomagnética - USANDO NOMBRES CORRECTOS
    cursor.execute('''
        SELECT fecha, tipo_evento, intensidad, fuente
        FROM solar_activity 
        WHERE fecha >= '2025-08-01' 
        ORDER BY fecha DESC
    ''')
    geomag_data = cursor.fetchall()
    
    # Datos de brotes de Ébola (simulados)
    ebola_outbreaks = [
        {'date': '2025-08-15', 'cases': 45, 'region': 'AAS', 'intensity': 'high'},
        {'date': '2025-08-22', 'cases': 78, 'region': 'AAS', 'intensity': 'very_high'},
        {'date': '2025-09-01', 'cases': 120, 'region': 'AAS', 'intensity': 'extreme'}
    ]
    
    # Buscar correlaciones
    correlations = []
    for outbreak in ebola_outbreaks:
        outbreak_date = datetime.strptime(outbreak['date'], '%Y-%m-%d')
        
        # Buscar actividad solar 3 días antes del brote
        for solar_event in geomag_data:
            try:
                event_date = datetime.strptime(solar_event[0], '%Y-%m-%d %H:%M:%S')
                time_diff = (outbreak_date - event_date).days
                
                if 0 <= time_diff <= 3:  # Ventana de 3 días
                    correlation_strength = calculate_correlation_strength(solar_event, outbreak)
                    
                    correlations.append({
                        'outbreak_date': outbreak['date'],
                        'solar_event_date': solar_event[0],
                        'time_diff_days': time_diff,
                        'event_type': solar_event[1],
                        'intensity': solar_event[2],
                        'source': solar_event[3],
                        'ebola_cases': outbreak['cases'],
                        'correlation_strength': correlation_strength
                    })
            except:
                continue
    
    conn.close()
    return sorted(correlations, key=lambda x: x['correlation_strength'], reverse=True)

def calculate_correlation_strength(solar_event, outbreak):
    """Calcular fuerza de correlación - VERSIÓN SIMPLIFICADA"""
    strength = 0
    
    # Tormentas geomagnéticas correlacionan más
    if 'geomagnetica' in solar_event[1].lower():
        strength += 0.6
    
    # Llamaradas solares también correlacionan
    if 'llamarada' in solar_event[1].lower():
        strength += 0.4
    
    # Alta intensidad
    if solar_event[2] and solar_event[2] > 5.0:
        strength += 0.3
    
    # Ajustar por número de casos
    strength *= (outbreak['cases'] / 100)
    
    return min(strength, 1.0)

if __name__ == "__main__":
    results = analyze_saa_correlations()
    print("🔬 RESULTADOS DEL ANÁLISIS AAS-ÉBOLA (CORREGIDO)")
    print("=================================================")
    
    if results:
        for i, correlation in enumerate(results[:5]):
            print(f"\n📊 Correlación #{i+1}:")
            print(f"   Fuerza: {correlation['correlation_strength']:.2f}")
            print(f"   Brote: {correlation['outbreak_date']} - {correlation['ebola_cases']} casos")
            print(f"   Evento solar: {correlation['solar_event_date']}")
            print(f"   Tipo: {correlation['event_type']}")
            print(f"   Intensidad: {correlation['intensity']}")
            print(f"   Diferencia temporal: {correlation['time_diff_days']} días")
    else:
        print("❌ No se encontraron correlaciones significativas")

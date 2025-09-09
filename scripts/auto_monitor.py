#!/usr/bin/env python3
import sqlite3
import requests
import time
from datetime import datetime
import random

class SpaceWeatherMonitor:
    def __init__(self, db_path):
        self.db_path = db_path
        self.api_urls = {
            'nasa': 'https://api.nasa.gov/DONKI/CME?api_key=DEMO_KEY',
            'noaa': 'https://services.swpc.noaa.gov/json/solar-cycle/observed-solar-cycle-indices.json'
        }
    
    def fetch_space_data(self):
        """Simular obtención de datos del clima espacial"""
        # En una implementación real, aquí se conectaría a APIs de NASA/NOAA
        return {
            'wind_speed': random.uniform(400, 600),
            'wind_density': random.uniform(0.1, 0.5),
            'bt_field': random.uniform(10, 20),
            'bz_field': random.uniform(-10, 10),
            'kp_index': random.randint(0, 9),
            'solar_flux': random.choice(['A1.5', 'B2.0', 'C1.8', 'M2.5', 'X1.0']),
            'aurora_level': random.choice(['Baja', 'Moderada', 'Alta', 'Muy Alta'])
        }
    
    def update_disease_cases(self):
        """Actualizar casos de enfermedades basado en actividad solar"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Obtener actividad solar reciente
        cursor.execute('SELECT kp_index, solar_flux FROM space_weather ORDER BY timestamp DESC LIMIT 1')
        latest_weather = cursor.fetchone()
        
        if latest_weather:
            kp_index, solar_flux = latest_weather
            
            # Calcular factor de aumento basado en actividad solar
            increase_factor = 1.0
            if kp_index > 5:
                increase_factor += (kp_index - 5) * 0.2
            if 'M' in solar_flux or 'X' in solar_flux:
                increase_factor += 0.5
            
            # Actualizar casos
            cursor.execute('''
                UPDATE hemorrhagic_diseases 
                SET cases_reported = cases_reported * ?,
                    solar_activity_level = ?
                WHERE correlation_strength > 0.7
            ''', (increase_factor, kp_index / 9.0))
            
            conn.commit()
        
        conn.close()
    
    def run_monitoring(self):
        """Ejecutar monitoreo continuo"""
        print("🚀 Iniciando monitoreo automático de clima espacial...")
        
        while True:
            try:
                # Obtener datos actuales
                space_data = self.fetch_space_data()
                
                # Guardar en base de datos
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT INTO space_weather 
                    (wind_speed, wind_density, bt_field, bz_field, kp_index, solar_flux, aurora_level)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    space_data['wind_speed'],
                    space_data['wind_density'],
                    space_data['bt_field'],
                    space_data['bz_field'],
                    space_data['kp_index'],
                    space_data['solar_flux'],
                    space_data['aurora_level']
                ))
                
                conn.commit()
                conn.close()
                
                # Actualizar casos de enfermedades
                self.update_disease_cases()
                
                print(f"📊 Datos actualizados: Kp{space_data['kp_index']} - {space_data['solar_flux']}")
                
                # Esperar 5 minutos antes de la próxima actualización
                time.sleep(300)
                
            except Exception as e:
                print(f"❌ Error en monitoreo: {e}")
                time.sleep(60)

if __name__ == "__main__":
    monitor = SpaceWeatherMonitor('/home/min/Heliobiologia.app/data/app.db')
    monitor.run_monitoring()

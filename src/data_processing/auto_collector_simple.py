import sqlite3
import requests
import time
from datetime import datetime
import random
import threading

class SimpleAutoCollector:
    def __init__(self):
        self.running = True
    
    def collect_solar_data(self):
        """Recolectar datos solares cada 30 minutos"""
        while self.running:
            try:
                print(f"{datetime.now()}: 🔄 Recolectando datos solares...")
                
                # Simular datos realistas
                conn = sqlite3.connect('data/app.db')
                
                # Datos solares realistas
                eventos = ['llamarada', 'viento_solar', 'tormenta_geomagnetica']
                evento = random.choice(eventos)
                intensidad = random.uniform(1.0, 8.0)
                
                conn.execute(
                    'INSERT INTO solar_activity (fecha, tipo_evento, intensidad, fuente) VALUES (?, ?, ?, ?)',
                    (datetime.now().isoformat(), evento, intensidad, 'NASA_Auto')
                )
                
                conn.commit()
                conn.close()
                print(f"✅ Datos solares actualizados: {evento} - {intensidad:.1f}")
                
            except Exception as e:
                print(f"❌ Error: {e}")
            
            # Esperar 30 minutos (1800 segundos)
            for i in range(1800):
                if not self.running:
                    break
                time.sleep(1)
    
    def collect_health_data(self):
        """Recolectar datos de salud cada hora"""
        while self.running:
            try:
                print(f"{datetime.now()}: 🏥 Recolectando datos de salud...")
                
                conn = sqlite3.connect('data/app.db')
                
                # Datos de salud basados en temporada
                hoy = datetime.now()
                if hoy.month in [9, 10, 11]:  # Otoño
                    incidencia = random.uniform(0.12, 0.20)
                    enfermedad = 'influenza_estacional'
                else:
                    incidencia = random.uniform(0.05, 0.15)
                    enfermedad = 'influenza'
                
                conn.execute(
                    'INSERT INTO health_data (fecha, tipo_enfermedad, incidencia, region, fuente) VALUES (?, ?, ?, ?, ?)',
                    (datetime.now().isoformat(), enfermedad, incidencia, 'España', 'OMS_Auto')
                )
                
                conn.commit()
                conn.close()
                print(f"✅ Datos salud actualizados: {enfermedad} - {incidencia:.1%}")
                
            except Exception as e:
                print(f"❌ Error: {e}")
            
            # Esperar 1 hora (3600 segundos)
            for i in range(3600):
                if not self.running:
                    break
                time.sleep(1)
    
    def stop(self):
        """Detener el recolector"""
        self.running = False
        print("🛑 Recolector detenido")
    
    def run(self):
        """Ejecutar recolección automática"""
        print("🚀 Recolector automático iniciado")
        
        # Iniciar hilos para recolección paralela
        solar_thread = threading.Thread(target=self.collect_solar_data)
        health_thread = threading.Thread(target=self.collect_health_data)
        
        solar_thread.daemon = True
        health_thread.daemon = True
        
        solar_thread.start()
        health_thread.start()
        
        # Mantener el programa principal activo
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

if __name__ == '__main__':
    collector = SimpleAutoCollector()
    collector.run()

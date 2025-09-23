import time
import sqlite3
from datetime import datetime
from chizhevsky_correlations import ChizhevskyCorrelationEngine

class ContinuousAnalyzer:
    def __init__(self):
        self.engine = ChizhevskyCorrelationEngine()
        self.analysis_interval = 3600  # 1 hora
        
    def run_continuous_analysis(self):
        """Ejecutar análisis continuo"""
        print("🔬 Iniciando analizador continuo de correlaciones Chizhevsky")
        
        while True:
            try:
                print(f"{datetime.now()}: 🔄 Ejecutando análisis...")
                
                # Calcular correlaciones
                correlations = self.engine.calculate_advanced_correlations()
                insights = self.engine.generate_heliobiological_insights(correlations)
                
                # Guardar resultados en base de datos
                conn = sqlite3.connect('data/app.db')
                for key, corr_data in correlations.items():
                    if corr_data['significativo']:
                        conn.execute('''
                            INSERT OR REPLACE INTO correlation_analysis 
                            (evento, enfermedad, correlacion, p_valor, retardo, timestamp)
                            VALUES (?, ?, ?, ?, ?, ?)
                        ''', (key, corr_data['correlacion_directa'], 
                              corr_data['p_valor_directa'], corr_data['retardo_optimo'],
                              datetime.now().isoformat()))
                
                conn.commit()
                conn.close()
                
                print(f"✅ Análisis completado: {len(insights)} insights significativos")
                
                # Esperar hasta el próximo análisis
                time.sleep(self.analysis_interval)
                
            except Exception as e:
                print(f"❌ Error en análisis: {e}")
                time.sleep(300)  # Esperar 5 minutos antes de reintentar

if __name__ == '__main__':
    analyzer = ContinuousAnalyzer()
    analyzer.run_continuous_analysis()

import sqlite3
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from scipy import stats

class ChizhevskyCorrelationEngine:
    def __init__(self):
        self.correlations = {}
        
    def calculate_advanced_correlations(self):
        """Calcular correlaciones basadas en los principios de Chizhevsky"""
        conn = sqlite3.connect('data/app.db')
        
        # Obtener datos de los últimos 90 días
        solar_data = pd.read_sql_query('''
            SELECT fecha, tipo_evento, intensidad 
            FROM solar_activity 
            WHERE fecha >= datetime('now', '-90 days')
            ORDER BY fecha
        ''', conn)
        
        health_data = pd.read_sql_query('''
            SELECT fecha, tipo_enfermedad, incidencia
            FROM health_data 
            WHERE fecha >= datetime('now', '-90 days')
            ORDER BY fecha
        ''', conn)
        
        # Convertir fechas
        solar_data['fecha'] = pd.to_datetime(solar_data['fecha'])
        health_data['fecha'] = pd.to_datetime(health_data['fecha'])
        
        # Análisis por tipo de evento solar
        correlations = {}
        
        for evento_solar in ['llamarada', 'viento_solar', 'tormenta_geomagnetica']:
            for enfermedad in health_data['tipo_enfermedad'].unique():
                # Filtrar datos
                solar_filtered = solar_data[solar_data['tipo_evento'] == evento_solar]
                health_filtered = health_data[health_data['tipo_enfermedad'] == enfermedad]
                
                # Agrupar por día y calcular promedios
                solar_daily = solar_filtered.groupby(solar_filtered['fecha'].dt.date)['intensidad'].mean()
                health_daily = health_filtered.groupby(health_filtered['fecha'].dt.date)['incidencia'].mean()
                
                # Alinear series temporales
                merged_data = pd.merge(solar_daily, health_daily, 
                                     left_index=True, right_index=True, how='inner')
                
                if len(merged_data) > 10:  # Mínimo de puntos para correlación
                    # Correlación directa
                    corr, p_value = stats.pearsonr(merged_data['intensidad'], merged_data['incidencia'])
                    
                    # Correlación con retardo (0-7 días)
                    max_corr = 0
                    best_lag = 0
                    for lag in range(8):
                        shifted_health = merged_data['incidencia'].shift(lag)
                        valid_data = pd.concat([merged_data['intensidad'], shifted_health], axis=1).dropna()
                        if len(valid_data) > 5:
                            lag_corr, _ = stats.pearsonr(valid_data['intensidad'], valid_data['incidencia'])
                            if abs(lag_corr) > abs(max_corr):
                                max_corr = lag_corr
                                best_lag = lag
                    
                    correlations[f"{evento_solar}_{enfermedad}"] = {
                        'correlacion_directa': corr,
                        'p_valor_directa': p_value,
                        'correlacion_maxima': max_corr,
                        'retardo_optimo': best_lag,
                        'muestras': len(merged_data),
                        'significativo': p_value < 0.05
                    }
        
        conn.close()
        return correlations
    
    def generate_heliobiological_insights(self, correlations):
        """Generar insights basados en la heliobiología"""
        insights = []
        
        for key, corr_data in correlations.items():
            if corr_data['significativo']:
                evento, enfermedad = key.split('_', 1)
                
                # Interpretación basada en Chizhevsky
                if corr_data['correlacion_directa'] > 0.3:
                    insight = f"📈 ALERTA: {evento} solar correlaciona positivamente con {enfermedad} "
                    insight += f"(r={corr_data['correlacion_directa']:.2f}, p={corr_data['p_valor_directa']:.3f})"
                    insights.append(insight)
                
                elif corr_data['correlacion_directa'] < -0.3:
                    insight = f"📉 INTERESANTE: {evento} solar correlaciona inversamente con {enfermedad} "
                    insight += f"(r={corr_data['correlacion_directa']:.2f})"
                    insights.append(insight)
        
        return insights

# Ejemplo de uso
if __name__ == '__main__':
    engine = ChizhevskyCorrelationEngine()
    correlations = engine.calculate_advanced_correlations()
    insights = engine.generate_heliobiological_insights(correlations)
    
    print("=== 🔬 CORRELACIONES CHIZHEVSKY ===")
    for insight in insights:
        print(insight)

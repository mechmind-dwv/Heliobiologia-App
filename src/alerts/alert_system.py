class LocalAlertSystem:
    def __init__(self):
        self.thresholds = {
            'solar_flare': 3.0,
            'solar_wind': 550.0,
            'health_correlation': 0.7
        }
    
    def check_alerts(self, solar_data, health_data):
        alerts = []
        
        # Verificar tormentas solares
        if solar_data.get('intensidad', 0) > self.thresholds['solar_flare']:
            alerts.append({
                'type': 'solar_storm',
                'level': 'warning',
                'message': 'Posible tormenta solar detectada'
            })
        
        # Verificar correlaciones de salud
        correlation = self.calculate_correlation(solar_data, health_data)
        if correlation > self.thresholds['health_correlation']:
            alerts.append({
                'type': 'health_correlation',
                'level': 'info',
                'message': f'Correlación significativa detectada: {correlation:.2f}'
            })
        
        return alerts
    
    def calculate_correlation(self, solar_data, health_data):
        """Cálculo simple de correlación local"""
        # Implementar algoritmo estadístico básico
        return 0.65  # Valor de ejemplo

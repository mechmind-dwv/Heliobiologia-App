from flask import Blueprint, jsonify
from ...data_processing.chizhevsky_correlations import ChizhevskyCorrelationEngine
from datetime import datetime

correlation_bp = Blueprint('correlations', __name__)

@correlation_bp.route('/api/correlations')
def get_correlations():
    """Endpoint para obtener correlaciones avanzadas"""
    try:
        engine = ChizhevskyCorrelationEngine()
        correlations = engine.calculate_advanced_correlations()
        insights = engine.generate_heliobiological_insights(correlations)
        
        return jsonify({
            'timestamp': datetime.now().isoformat(),
            'correlations': correlations,
            'insights': insights,
            'stats': {
                'total_correlations': len(correlations),
                'significant_correlations': len([c for c in correlations.values() if c['significativo']]),
                'last_analysis': datetime.now().isoformat()
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@correlation_bp.route('/api/chizhevsky-principles')
def get_principles():
    """Endpoint con los principios de Chizhevsky"""
    return jsonify({
        'principles': [
            {
                'principle': 'Sincronización cósmica',
                'description': 'Los organismos vivos están sincronizados con los ritmos solares y cósmicos',
                'evidence': 'Ciclos circadianos, estacionales y solares en fisiología humana'
            },
            {
                'principle': 'Correlación actividad solar-salud',
                'description': 'La actividad solar influye en los sistemas cardiovascular, nervioso e inmunológico',
                'evidence': 'Estudios epidemiológicos sobre tormentas geomagnéticas y salud'
            },
            {
                'principle': 'Historia humana y ciclos solares',
                'description': 'Los eventos históricos masivos correlacionan con máximos de actividad solar',
                'evidence': 'Análisis de Chizhevsky de 2500 años de historia'
            }
        ]
    })

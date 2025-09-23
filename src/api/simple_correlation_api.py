from flask import Blueprint, jsonify
from src.data_processing.simple_correlations import get_simple_correlations

simple_bp = Blueprint('simple_correlations', __name__)

@simple_bp.route('/api/simple-correlations')
def simple_correlations():
    """Endpoint simplificado y funcional"""
    return jsonify(get_simple_correlations())

@simple_bp.route('/api/chizhevsky-insights')
def chizhevsky_insights():
    """Insights basados en Chizhevsky"""
    return jsonify({
        'insights': [
            '🌞 La actividad solar muestra correlación con indicadores de salud pública',
            '📈 Períodos de alta actividad solar pueden influir en el sistema inmunológico',
            '🔬 Según Chizhevsky: Los máximos solares correlacionan con eventos históricos',
            '🏥 Influenza estacional muestra patrones relacionados con ciclos solares',
            '⚠️ Tormentas geomagnéticas pueden afectar sistemas cardiovasculares'
        ],
        'principles': [
            'Sincronización cósmica organismo-entorno',
            'Influencia solar en biorritmos humanos', 
            'Correlación actividad solar-salud poblacional',
            'Ciclos históricos y ciclos solares'
        ]
    })

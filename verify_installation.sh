#!/bin/bash
# ✅ Script de verificación completa

echo "🌌 VERIFICACIÓN COMPLETA DEL SISTEMA"
echo "======================================"

# 1. Verificar Python
echo "🐍 Python: $(python --version)"

# 2. Verificar dependencias
echo "📦 Dependencias:"
python -c "
import flask, requests, numpy, pandas, sqlite3
print('   Flask:', flask.__version__)
print('   Requests:', requests.__version__)
print('   Numpy:', numpy.__version__)
print('   Pandas:', pandas.__version__)
print('   SQLite3:', sqlite3.version)
"

# 3. Verificar estructura
echo "📁 Estructura:"
echo "   - src/: $(find src/ -name '*.py' | wc -l) archivos Python"
echo "   - scripts/: $(find scripts/ -name '*.sh' | wc -l) scripts"
echo "   - data/: $(ls -la data/ 2>/dev/null | wc -l) archivos"

# 4. Verificar base de datos
echo "🗃️ Base de datos:"
if [ -f "data/app.db" ]; then
    python -c "
import sqlite3
conn = sqlite3.connect('data/app.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM sqlite_master')
print('   ✅ Base de datos operativa')
conn.close()
"
else
    echo "   ⚠️ Base de datos no encontrada"
fi

echo "======================================"
echo "✅ Verificación completada"

#!/usr/bin/env python3
import os

paths_to_check = [
    '/home/min/Heliobiologia.app/data/app.db',
    '/home/min/Heliobiologia.app/src/api/local_api.py',
    '/home/min/Heliobiologia.app/src/data_processing/data_collector.py'
]

print("🔍 Verificación de Rutas Absolutas")
for path in paths_to_check:
    status = "✅ EXISTE" if os.path.exists(path) else "❌ NO EXISTE"
    print(f"{status}: {path}")

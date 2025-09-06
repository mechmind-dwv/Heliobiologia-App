#!/usr/bin/env python3
import os
import sqlite3

print("🔍 VERIFICACIÓN DE RUTAS CRÍTICAS")

# Ruta correcta de la base de datos
db_path = "/home/min/Heliobiologia.app/data/app.db"
print(f"🗃️  Base de datos: {db_path}")
if os.path.exists(db_path):
    print("   ✅ EXISTE")
    try:
        conn = sqlite3.connect(db_path)
        print("   ✅ CONEXIÓN EXITOSA")
        conn.close()
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
else:
    print("   ❌ NO EXISTE - Creando...")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    open(db_path, 'w').close()
    print("   ✅ CREADA")

# Verificar archivos esenciales
essential_files = [
    "src/api/local_api.py",
    "src/data_processing/data_collector.py", 
    "src/web_interface/app.py"
]

for file in essential_files:
    full_path = f"/home/min/Heliobiologia.app/{file}"
    status = "✅ EXISTE" if os.path.exists(full_path) else "❌ NO EXISTE"
    print(f"📄 {file}: {status}")

#!/bin/bash

echo "🔄 Actualizando Heliobiología.app"

cd ~/heliobiologia-app

# Actualizar desde git (cuando corresponda)
# git pull origin main

# Actualizar dependencias
pip3 install -r requirements.txt

# Actualizar base de datos
sqlite3 data/app.db "VACUUM;"

echo "✅ Actualización completada"

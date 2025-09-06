#!/bin/bash

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="./data/backups/$TIMESTAMP"

mkdir -p $BACKUP_DIR

# Respaldar base de datos
sqlite3 data/app.db ".backup '$BACKUP_DIR/app.db.bak'"

# Respaldar configuraciones
cp -r config/ $BACKUP_DIR/

echo "📦 Backup creado: $BACKUP_DIR"

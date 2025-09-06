#!/bin/bash
BACKUP_DIR="/home/min/Heliobiologia.app/backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p $BACKUP_DIR

# Backup de código
tar -czf $BACKUP_DIR/code_backup.tar.gz src/ config/ scripts/

# Backup de datos
sqlite3 data/app.db ".backup '$BACKUP_DIR/app.db.bak'"

# Verificación de backup
echo "📦 BACKUP COMPLETADO: $BACKUP_DIR" >> docs/BACKUP_LOG.md
echo "📊 Tamaño: $(du -sh $BACKUP_DIR | awk '{print $1}')" >> docs/BACKUP_LOG.md
echo "🔒 Checksum: $(tar -cf - $BACKUP_DIR | sha256sum)" >> docs/BACKUP_LOG.md

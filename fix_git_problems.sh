#!/bin/bash
echo "🔧 SOLUCIONADOR DE PROBLEMAS GIT"
cd ~/Heliobiologia-App
git pull origin main --allow-unrelated-histories
git add .
git commit -m "🔄 Fix: $(date)"
git push origin main
echo "✅ Problemas solucionados!"

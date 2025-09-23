#!/bin/bash
# 🌌 Script de instalación Heliobiología.app
# Tributo a Alexander Chizhevsky

echo "❤️  INSTALANDO HELIOBIOLOGÍA.APP..."

# Crear directorio
mkdir -p ~/chizhevsky_cosmic_lab
cd ~/chizhevsky_cosmic_lab

# Clonar repositorio
if [ ! -d "Heliobiologia-App" ]; then
    git clone https://github.com/mechmind-dwv/Heliobiologia-App.git
fi

cd Heliobiologia-App

# Verificar commit específico
git checkout 8592c25df17257f660cd98e2644e661e6d22e110

# Entorno virtual
python3 -m venv chizhevsky_venv
source chizhevsky_venv/bin/activate

# Instalar dependencias
pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    pip install flask requests numpy pandas python-dotenv
fi

# Permisos
chmod +x *.sh 2>/dev/null
chmod +x scripts/*.sh 2>/dev/null

echo "🎉 INSTALACIÓN COMPLETADA"
echo "📍 Ubicación: $(pwd)"
echo "🐍 Entorno: chizhevsky_venv"
echo "🌐 Ejecutar: source chizhevsky_venv/bin/activate"
echo "🚀 Iniciar: python src/api/local_api.py"

# 📊 Estado Actual del Sistema - Heliobiología.app

## 🖥️ Especificaciones del Equipo Local
$(lscpu | grep "Model name\|Architecture\|CPU(s)")
$(free -h | grep "Mem:\|Swap:")
$(df -h / | grep -v File)

## 📦 Dependencias Instaladas
$(pip list | grep -E "flask|pandas|numpy|requests|sqlalchemy")

## 🗃️ Base de Datos
$(sqlite3 data/app.db ".tables" 2>/dev/null || echo "Base de datos no inicializada")

## 🌐 Servicios Activos
$(netstat -tulpn | grep :5000 || echo "Puerto 5000 no ocupado")
$(netstat -tulpn | grep :8080 || echo "Puerto 8080 no ocupado")

## 🔍 Últimos Errores
$(tail -n 20 mechbot_session.log 2>/dev/null || echo "Log no disponible")


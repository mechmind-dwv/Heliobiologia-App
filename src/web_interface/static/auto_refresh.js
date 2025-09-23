// Auto-recarga cada 30 segundos
console.log('✅ Script de auto-actualización cargado');

function actualizarDatos() {
    console.log('🔄 Actualizando datos...');
    
    // Actualizar datos solares
    fetch('/api/solar-data')
        .then(response => response.json())
        .then(data => {
            if(data && data.length > 0) {
                const solarCount = document.querySelector('[data-solar-count]');
                const latestSolar = document.querySelector('[data-latest-solar]');
                
                if(solarCount) solarCount.textContent = data.length;
                if(latestSolar) {
                    const latest = data[0];
                    latestSolar.textContent = 
                        `${latest.tipo_evento} - ${latest.intensidad} - ${latest.fuente}`;
                }
            }
        })
        .catch(error => console.error('Error solar:', error));
    
    // Actualizar datos de salud
    fetch('/api/health-data')
        .then(response => response.json())
        .then(data => {
            if(data && data.length > 0) {
                const healthCount = document.querySelector('[data-health-count]');
                const latestHealth = document.querySelector('[data-latest-health]');
                
                if(healthCount) healthCount.textContent = data.length;
                if(latestHealth) {
                    const latest = data[0];
                    latestHealth.textContent = 
                        `${latest.tipo_enfermedad} - ${(latest.incidencia * 100).toFixed(1)}% - ${latest.region}`;
                }
            }
        })
        .catch(error => console.error('Error salud:', error));
    
    // Actualizar hora
    const updateTime = document.querySelector('[data-update-time]');
    if(updateTime) {
        updateTime.textContent = new Date().toLocaleString();
    }
}

// Ejecutar inmediatamente y cada 30 segundos
actualizarDatos();
setInterval(actualizarDatos, 30000);

console.log('🔄 Auto-actualización configurada cada 30 segundos');

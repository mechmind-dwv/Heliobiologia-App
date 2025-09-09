#!/usr/bin/env python3
import sqlite3
import sys
from datetime import datetime

def check_database():
    try:
        conn = sqlite3.connect('/home/min/Heliobiologia.app/data/app.db')
        cursor = conn.cursor()
        
        # Check solar_activity table
        cursor.execute("SELECT COUNT(*) FROM solar_activity")
        solar_count = cursor.fetchone()[0]
        
        # Check health_data table
        cursor.execute("SELECT COUNT(*) FROM health_data")
        health_count = cursor.fetchone()[0]
        
        # Check recent data
        cursor.execute("""
            SELECT COUNT(*) FROM solar_activity 
            WHERE fecha >= datetime('now', '-7 days')
        """)
        recent_solar = cursor.fetchone()[0]
        
        print(f"📊 ESTADO DE LA BASE DE DATOS:")
        print(f"   Eventos solares totales: {solar_count}")
        print(f"   Registros de salud: {health_count}")
        print(f"   Eventos últimos 7 días: {recent_solar}")
        
        if solar_count > 0:
            # Show sample data
            cursor.execute("""
                SELECT tipo_evento, intensidad, fecha 
                FROM solar_activity 
                ORDER BY fecha DESC 
                LIMIT 5
            """)
            print(f"\n📈 ÚLTIMOS EVENTOS SOLARES:")
            for row in cursor.fetchall():
                print(f"   {row[0]} - Intensidad: {row[1]} - {row[2]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Error en la base de datos: {e}")
        return False

if __name__ == "__main__":
    success = check_database()
    sys.exit(0 if success else 1)

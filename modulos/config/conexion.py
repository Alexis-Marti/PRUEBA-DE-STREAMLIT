import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='bvn6dva9xsto1mq6ufhl-mysql.services.clever-cloud.com',
            user='ukkz6pv0aivbzwu0',
            password='wsEyEErBr88Ac7l3cFkG',
            database='bvn6dva9xsto1mq6ufhl',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None

import mysql.connector
import os

def conectar_db():
    # Obtener las credenciales de las variables de entorno (seguridad)
    host = os.getenv("DB_HOST", "bvn6dva9xsto1mq6ufhl-mysql.services.clever-cloud.com")
    user = os.getenv("DB_USER", "ukkz6pv0aivbzwu0")
    password = os.getenv("DB_PASSWORD", "wsEyEErBr88Ac7l3cFkG")
    database = os.getenv("DB_NAME", "bvn6dva9xsto1mq6ufhl")

    # Intentar establecer la conexión
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Verificar si la conexión fue exitosa
        if conn.is_connected():
            return conn
        else:
            return None
    except mysql.connector.Error as err:
        return None, f"Error al conectar con la base de datos: {err}"

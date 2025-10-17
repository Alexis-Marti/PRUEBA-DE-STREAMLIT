import mysql.connector
import os

def conectar_db():
    # Obtener las credenciales de las variables de entorno (seguridad)
    host = os.getenv("DB_HOST", "be5bmntqvmjb45dbc68h-mysql.services.clever-cloud.com")
    user = os.getenv("DB_USER", "ufrsewvahgrdaghy")
    password = os.getenv("DB_PASSWORD", "UxDnJbPxibZaLwBC6Xt1")
    database = os.getenv("DB_NAME", "be5bmntqvmjb45dbc68h")

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

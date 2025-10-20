import mysql.connector
from mysql.connector import Error
from modulos.config.conexion import obtener_conexion

def login(usuario, contrasena):
    try:
        conexion = obtener_conexion()
        if conexion is None:
            return "❌ No se pudo establecer la conexión"

        cursor = conexion.cursor()
        # Ajustamos la consulta para que coincida con la tabla 'empleado'
        query = "SELECT * FROM empleado WHERE usuario = %s AND contrasena = %s"
        cursor.execute(query, (usuario, contrasena))
        resultado = cursor.fetchone()

        if resultado:
            print("✅ Login exitoso")
            return True
        else:
            print("❌ Usuario o contraseña incorrectos")
            return False

    except mysql.connector.Error as e:
        print(f"❌ Error al ejecutar la consulta: {e}")
        return False
    finally:
        if conexion and conexion.is_connected():
            cursor.close()
            conexion.close()

# Ejemplo de uso
if __name__ == "__main__":
    usuario_input = input("Usuario: ")
    contrasena_input = input("Contraseña: ")
    if login(usuario_input, contrasena_input):
        print("Acceso concedido")
    else:
        print("Acceso denegado")

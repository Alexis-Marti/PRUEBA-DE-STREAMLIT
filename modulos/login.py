def verificar_usuario(Usuario, Contra):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None

    try:
        cursor = con.cursor()
        query = "SELECT * FROM Empleados WHERE Usuario = %s AND Contra = %s"
        cursor.execute(query, (Usuario, Contra))
        result = cursor.fetchone()
        
        if result:  # Si encontramos un resultado
            return result
        else:
            return None  # No se encontraron resultados

    except mysql.connector.Error as err:
        st.error(f"Error al ejecutar la consulta: {err}")
        st.error(f"Consulta SQL: {query}")
        return None
    finally:
        con.close()


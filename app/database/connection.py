import sqlite3
from sqlite3 import Error

def create_connection():
    """
    Crea la conexion a la base de datos
    """
    conn = None
    try:
        conn = sqlite3.connect("database/table_data.db") #crea la base de datos
        print("Se creo la base de datos")
    
    except Error as e:
        print("Error al conectar con la base de datos")

    return conn
    
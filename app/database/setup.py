from importlib.resources import path
import sqlite3
from sqlite3 import Error
from .connection import create_connection

def read_file(path):
    """
    Funcion Para leer el archivo .sql
    """
    with open(path, 'r') as sql_file:
        return sql_file.read()

def create_table():
    """
    Funcion para crear la base de datos
    """
    conn = create_connection() # funcion que esta en connection.py
    path = "database/sql/tables.sql" # Ruta donde esta el arhivo .sql
    sql = read_file(path) #lee el archivo con la ruta dada

    try:
        cur = conn.cursor()
        cur.executescript(sql) # ejecuta todo un script
        conn.commit()
        print("Entre en el try de la creacion de las tablas")
        return True
    
    except Error as e:
        print(f"hubo un error al crear las tablas {e}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

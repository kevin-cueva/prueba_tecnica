import sqlite3
from sqlite3 import Error

from .connection import create_connection

def insert_data_esp_marinas(lug,esp,avis,date,time):
    """
    Funcion de prueba para insertar datos en especies_marinas
    """
    conn = create_connection()

    sql = f"""INSERT INTO "especies_marinas"
              ("lugar", "especie", "avistamiento", "created_date", "created_time")
              VALUES ('{lug}', '{esp}', '{avis}', '{date}', '{time}');"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTO")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the insert_data() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_data_lugares(id, pais, dep, ciudad, nom_lugar):
    """
    Funcion de prueba para insertar dato en la tabla lugares
    """
    conn = create_connection()

    sql = f"""INSERT INTO "lugares"
              ("id_lugar", "pais", "departamento", "ciudad", "nombre_del_lugar")
              VALUES ('{id}', '{pais}', '{dep}', '{ciudad}', '{nom_lugar}');"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTO")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the insert_data() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_data_avistamiento(id, nom_cien, lugar, lati, longitub, autor, nota):

    """
    Funcion de prueba para insertar dato en la tabla avistamiento
    """
    conn = create_connection()

    sql = f"""INSERT INTO "avistamientos"
              ("id_avistamientos", "nombre_cientifico", "lugar", "latitud", "longitud", "autor", "notas")
              VALUES ('{id}', '{nom_cien}', '{lugar}','{lati}','{longitub}', '{autor}', '{nota}');"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTO")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the insert_data() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()  

def insert_data_cat_taxonomica(id, reino, filo, clase, orden, familia, genero, especie):
    """
    Funcion de prueba para insertar dato en la tabla categoria_taxonomica
    """
    conn = create_connection()

    sql = f"""INSERT INTO "categoria_taxonomica"
             ("id_taxonomica", "reino", "filo", "clase", "orden", "familia", "genero", "especie")
             VALUES ('{id}', '{reino}', '{filo}', '{clase}', '{orden}', '{familia}', '{genero}', '{especie}');"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTO")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the insert_data() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()  

def insert_data_especies(id, nom_comun, nom_cien, especie):

    """
    Funcion de prueba para insertar dato en la tabla especies
    """
    conn = create_connection()

    sql = f"""INSERT INTO "main"."especies"
              ("id_especie", "nombre_comun", "nombre_cientifico", "especie")
               VALUES ('{id}', '{nom_comun}', '{nom_cien}', '{especie}');"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTO")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the insert_data() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()  


#______ ELIMINACION ___________

def delete_especies(id):
    """
    Funcion para eliminar de lugares especie y avistamiento
    """   
    conn = create_connection()
    sql = f"""DELETE FROM especies WHERE id_especie = {id};"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTA ELIMINACION")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the delete_especies() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()  

def delete_cat_taxonomica(id):
    """
    Funcion para eliminar de lugares especie y avistamiento
    """   
    conn = create_connection()
    sql = f"""DELETE FROM categoria_taxonomica WHERE id_taxonomica = {id};"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTA ELIMINACION")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the delete_cat_taxonomica() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()  

def delete_avistamientos(id):
    """
    Funcion para eliminar de lugares especie y avistamiento
    """   
    conn = create_connection()
    sql = f"""DELETE FROM avistamientos WHERE id_avistamientos = {id};"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTA ELIMINACION")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the delete_avistamientos() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close() 

def delete_lugares(id):
    """
    Funcion para eliminar de lugares especie y avistamiento
    """   
    conn = create_connection()
    sql = f"""DELETE FROM lugares WHERE id_lugar = {id};"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTA ELIMINACION")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the delete_id_lugar() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_especies_marinas(id):
    """
    Funcion para eliminar de lugares especie y avistamiento
    """   
    conn = create_connection()
    sql = f"""DELETE FROM especies_marinas WHERE id_especies_marinas = {id};"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTA ELIMINACION")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the delete_id_lugar() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()  


#_____ ACTUALIZACION _______
def update_data_esp_marinas(id,lug,esp,avis,date,time):

    """
    Funcion Para Actualizar la especie marina
    """
    conn = create_connection()

    sql = f"""UPDATE "especies_marinas"
              SET lugar = '{lug}', especie = '{esp}', avistamiento = '{avis}', 
                  created_date = '{date}', created_time = '{time}'
              WHERE id_especies_marinas = {id};"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTO")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the update_esp_marinas() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()

def update_data_lugares(id, pais, dep, ciudad, nom_lugar):
    """
    Funcion de prueba para insertar dato en la tabla lugares
    """
    conn = create_connection()

    sql = f"""UPDATE "lugares"
              SET pais ='{pais}', departamento = '{dep}', 
              ciudad = '{ciudad}', nombre_del_lugar = '{nom_lugar}'
              WHERE id_lugar = '{id}';"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTO")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the update_data_lugares() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()            

def update_data_avistamiento(id, nom_cien, lugar, lati, longitub, autor, nota):

    """
    Funcion de prueba para actualizar dato en la tabla avistamiento
    """
    conn = create_connection()

    sql = f"""UPDATE "avistamientos"
              SET nombre_cientifico ='{nom_cien}', lugar ='{lugar}', latitud ='{lati}', 
              longitud ='{longitub}', autor ='{autor}', notas ='{nota}'
              WHERE id_avistamientos = '{id}';"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTO")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the update_data_avistamiento() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()

def update_data_cat_taxonomica(id, reino, filo, clase, orden, familia, genero, especie):
    """
    Funcion de prueba para actualizar dato en la tabla categoria_taxonomica
    """
    conn = create_connection()

    sql = f"""UPDATE "categoria_taxonomica"
             SET reino = '{reino}', filo = '{filo}', clase = '{clase}', orden = '{orden}', 
                 familia = '{familia}', genero = '{genero}', especie = '{especie}'
             WHERE id_taxonomica = '{id}';"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTO")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the update_data_cat_taxonomica() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()  

def update_data_especies(id, nom_comun, nom_cien, especie):

    """
    Funcion de prueba para insertar dato en la tabla especies
    """
    conn = create_connection()

    sql = f"""UPDATE "especies"
              SET nombre_comun = '{nom_comun}', nombre_cientifico = '{nom_cien}', especie = '{especie}'
              WHERE id_especie ='{id}';"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print ("CORRECTO")
        return cur.lastrowid #id del registro
    except Error as e:
        print(f"error at the update_data_especies() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()  


#____ CONSULTA DE LA ESPECIE ____

def consulta_especies(especie):

    """
    Funcion de prueba para hacer una consulta join con el parametro especie
    """
    conn = create_connection()

    sql = f"""SELECT avistamientos.nombre_cientifico, avistamientos.lugar,avistamientos.notas,
                     categoria_taxonomica.reino,categoria_taxonomica.familia,categoria_taxonomica.especie 
              FROM 'categoria_taxonomica'
              INNER JOIN 'avistamientos'
              ON avistamientos.id_avistamientos = categoria_taxonomica.id_taxonomica
              WHERE categoria_taxonomica.especie = '{especie}'
              ;"""
    
        
    try:
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        conn.commit()
        print ("CORRECTO")
        request_json = {"nombre_cientifico":f"{data[0][0]}", "lugar":f"{data[0][1]}",
                        "notas":f"{data[0][2]}", "reino":f"{data[0][3]}", "familia":f"{data[0][4]}",
                        "especie":f"{data[0][5]}"}
        
        print(request_json)
        return request_json 
    except Error as e:
        print(f"error at the consulta_especies() : {str(e)}")
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()  
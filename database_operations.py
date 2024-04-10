import csv
import sys
import MySQLdb
from MySQLdb import Error
from csv_operations import crear_archivos

def conectar_bd():
    try:
        db = MySQLdb.connect("localhost","root","","provincias")
        print("Conexión exitosa")
        return db
    except MySQLdb.Error as e:
        print("Falla en la conexión a la base de datos:",e)
        sys.exit(1)

def crear_tabla(db):
    try:
        cursor = db.cursor()
        sql="CREATE TABLE provincias(id INT AUTO_INCREMENT PRIMARY KEY, provincia VARCHAR(255), localidad VARCHAR(255), cp VARCHAR(10), id_prov_mstr INT)"
        cursor.execute("DROP TABLE IF EXISTS provincias")
        cursor.execute(sql)
        db.commit()
        print("Tabla creada con éxito")
    except Error as e:
        db.rollback()
        print("Error al crear la tabla",e)
        sys.exit(1)

def insertar_datos(db,archivo_csv):
    try:
        cursor = db.cursor()
        with open(archivo_csv, 'r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=',', quotechar='"')
            for fila in lector_csv:
                sql = "INSERT INTO provincias(provincia, cp, localidad, id_prov_mstr) VALUES(%s, %s, %s, %s)"
                cursor.execute(sql, (fila[0], fila[1], fila[2], fila[3]))
            db.commit()
            print("Datos insertados con éxito")
    except Error as e:
        print("Error al insertar los datos",e)

def eliminar_datos_innecesarios(db):
    try:
        
        cursor = db.cursor()
        sql = "DELETE FROM provincias WHERE id = 1 AND provincia = 'provincia' AND localidad = 'localidad' AND cp = 'id' AND id_prov_mstr = 0"
        cursor.execute(sql)
        db.commit()
        print("Datos innecesarios eliminados con éxito")
    except Error as e:
        print("Error al eliminar los datos innecesarios",e)
        sys.exit(1)

def agrupar_por_provincia(db):
    try:
        cursor = db.cursor()
        sql = "SELECT provincia, COUNT(*) FROM provincias GROUP BY provincia"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        provincias = {}
        for provincia, localidad in resultados:
            if provincia not in provincias:
                provincias[provincia] = []
                provincias[provincia].append(localidad)
        print("Datos agrupados con éxito")
        print(provincias)
        return provincias
    except Error as e:
        print("Error al agrupar los datos",e)
        return None
    


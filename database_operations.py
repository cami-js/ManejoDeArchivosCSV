import csv
import sys
import MySQLdb
from MySQLdb import Error

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
                sql = "INSERT INTO provincias(provincia, localidad, cp, id_prov_mstr) VALUES(%s, %s, %s, %s)"
                cursor.execute(sql, (fila[0], fila[1], fila[2], fila[3]))
            db.commit()
            print("Datos insertados con éxito")
    except Error as e:
        print("Error al insertar los datos",e)

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
    

    
    
    
    
    
    
    
    
    # finally:
    #     db.close()

if __name__ == '__main__':
    archivo_csv = 'localidades.csv'
    db = conectar_bd()
    crear_tabla(db)
    insertar_datos(db,archivo_csv)
    agrupar_por_provincia(db)
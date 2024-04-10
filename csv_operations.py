import csv
import sys

def leer_archivo(archivo_csv):
    try:
        with open('localidades.csv', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=',', quotechar='"')
            for fila in lector_csv:
                print(fila)
    except Exception as e:
        print("Error al leer el archivo",e)
        sys.exit(1)
with open('localidades.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',', quotechar='"')
    for fila in lector_csv:
        print(fila)

def crear_archivos(provincias, db):
    try:
        cursor = db.cursor()
        for provincia, cantidad in provincias.items():
            with open(f'{provincia}.csv', mode='w', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv, delimiter=',', quotechar='"')
                escritor_csv.writerow(['Localidad'])
                sql = "SELECT localidad FROM provincias WHERE provincia = %s"
                cursor.execute(sql, (provincia,))
                localidades = cursor.fetchall()

                for localidad in localidades:
                    escritor_csv.writerow([localidad])
                escritor_csv.writerow(['Cantidad de localidades:', cantidad])
            print(f"Archivo {provincia}.csv creado con éxito")
    except Exception as e:
        print("Error al crear los archivos",e)
        sys.exit(1) 
        

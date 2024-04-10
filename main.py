from database_operations import conectar_bd, crear_tabla, insertar_datos, eliminar_datos_innecesarios, agrupar_por_provincia
from csv_operations import crear_archivos

def main():
    archivo_csv = 'localidades.csv'
    
    # Conectar a la base de datos
    db = conectar_bd()
    
    # Crear tabla si no existe
    crear_tabla(db)
    
    # Insertar datos desde el archivo CSV a la base de datos
    insertar_datos(db, archivo_csv)
    
    # Eliminar datos innecesarios de la base de datos
    eliminar_datos_innecesarios(db)
    
    # Agrupar localidades por provincia
    provincias = agrupar_por_provincia(db)
    
    # Crear archivos CSV para cada provincia con sus localidades
    if provincias:
        crear_archivos(provincias, db)
    
    # Cerrar la conexión a la base de datos
    db.close()

if __name__ == '__main__':
    main()

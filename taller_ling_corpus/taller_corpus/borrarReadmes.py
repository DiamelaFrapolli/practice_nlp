import os

# Obtiene el directorio actual (donde se encuentra el script)
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Recorre todos los archivos en el directorio actual
for archivo in os.listdir(directorio_actual):
    # Verifica si el archivo tiene la extensión .readme
    if archivo.lower().endswith('.readme'):
        ruta_archivo = os.path.join(directorio_actual, archivo)
        # Intenta eliminar el archivo
        try:
            os.remove(ruta_archivo)
            print(f"Archivo eliminado: {archivo}")
        except Exception as e:
            print(f"No se pudo eliminar {archivo}. Error: {e}")

print("Proceso de eliminación completado.")

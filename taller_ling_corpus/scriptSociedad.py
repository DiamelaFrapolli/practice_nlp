import re

# Lee el contenido del archivo txt que contiene el código fuente de la página
archivo = "C:/Users/diame/OneDrive/Documentos/Proyectos/practice_nlp/taller_ling_corpus/codigoFuenteSociedad.txt"
with open(archivo, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Verifica que el archivo se haya leído correctamente
print("Contenido del archivo leído correctamente. Longitud del contenido:", len(html_content))

# Expresión regular para encontrar enlaces href
pattern = r'href="(http[^"]+)"'

# Encuentra todos los enlaces que coinciden con el patrón
enlaces = re.findall(pattern, html_content)

# Filtra enlaces para incluir solo los que pertenecen a 'lanacion.com.ar'
# Excluye enlaces que contienen parámetros típicos de resultados de búsqueda de Google
enlaces_filtrados = [
    enlace for enlace in enlaces
    if 'lanacion.com.ar' in enlace and not (
        'search' in enlace or
        'q=' in enlace or
        'source=' in enlace or
        'page=' in enlace or
        'url=' in enlace
    )
]

# Verifica que se encontraron enlaces
print(f"Se encontraron {len(enlaces_filtrados)} enlaces relevantes en el documento.")

# Imprime todos los enlaces relevantes encontrados
print("Enlaces relevantes encontrados:")
for enlace in enlaces_filtrados:
    print(enlace)


# Ordena los enlaces alfabéticamente
enlaces_filtrados.sort()

# Nombre del archivo de salida
archivo_salida = "C:/Users/diame/OneDrive/Documentos/Proyectos/practice_nlp/taller_ling_corpus/enlaces_sociedad.txt"

# Escribe los enlaces ordenados en el archivo de salida
with open(archivo_salida, 'w', encoding='utf-8') as file:
    for enlace in enlaces_filtrados:
        file.write(enlace + '\n')

# Verifica que se hayan escrito los enlaces en el archivo
print(f"Enlaces ordenados y guardados en {archivo_salida}.")
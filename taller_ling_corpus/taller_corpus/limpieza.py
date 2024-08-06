import os
from bs4 import BeautifulSoup

# Configuración de directorios
directorio_html = 'C:/Users/diame/OneDrive/Documentos/Proyectos/practice_nlp/taller_ling_corpus/taller_corpus'
directorio_txt = 'C:/Users/diame/OneDrive/Documentos/Proyectos/practice_nlp/taller_ling_corpus/txt_files'

# Asegúrate de que el directorio de salida existe
os.makedirs(directorio_txt, exist_ok=True)

# Recorre todos los archivos en el directorio de entrada
for archivo in os.listdir(directorio_html):
    if archivo.lower().endswith('.html'):
        ruta_html = os.path.join(directorio_html, archivo)
        
        # Lee el contenido del archivo HTML
        with open(ruta_html, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Analiza el contenido con BeautifulSoup
        soup = BeautifulSoup(html_content, 'lxml')

        # Elimina las etiquetas <script> y <style>
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()

        # Obtiene el texto limpio
        texto_limpio = soup.get_text(separator='\n').strip()

        # Nombre del archivo de salida
        nombre_archivo_txt = os.path.splitext(archivo)[0] + '.txt'
        ruta_txt = os.path.join(directorio_txt, nombre_archivo_txt)

        # Guarda el texto limpio en un archivo .txt
        with open(ruta_txt, 'w', encoding='utf-8') as file:
            file.write(texto_limpio)

        print(f'Archivo procesado: {archivo} -> {nombre_archivo_txt}')

print('Proceso completado.')

import requests
from bs4 import BeautifulSoup

# URL de la página principal de noticias de ciencia
url = "https://www.lanacion.com.ar/ciencia/"

# Realizar la solicitud GET para obtener el contenido de la página
response = requests.get(url)
response.raise_for_status()  # Asegura que la solicitud se completó correctamente

# Parsear el contenido HTML de la página
soup = BeautifulSoup(response.content, "html.parser")

# Encontrar todos los enlaces en la página
links = soup.find_all("a", href=True)

# Filtrar los enlaces que contienen "covid" o "coronavirus" en la URL
filtered_links = [link["href"] for link in links if "covid" in link["href"] or "coronavirus" in link["href"]]

# Imprimir los enlaces filtrados
for link in filtered_links:
    print(link)

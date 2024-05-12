
import requests
from bs4 import BeautifulSoup


def obtener_enlaces(url):
    try:
        # Obtener la página web
        response = requests.get(url)
        # Parsear la página con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Encontrar todos los enlaces en la página
        enlaces = soup.find_all('a')
        # Retornar una lista de enlaces que comienzan con 'http'
        return [enlace['href'] for enlace in enlaces if enlace.get('href') and enlace['href'].startswith('http')]
    except Exception as e:
        print("Error al obtener enlaces:", e)
        return []

# URL de la página que queremos hacer scraping
url = "https://www.google.com/https://www.google.com"

# Hacemos una solicitud GET a la URL
response = requests.get(url)

# Parseamos el contenido HTML utilizando Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Buscamos el título de la página
title = soup.find('title')
enlaces = soup.find_all('a')

# Imprimimos el título
# print(title.text)
# print(enlaces)

print(obtener_enlaces(url))
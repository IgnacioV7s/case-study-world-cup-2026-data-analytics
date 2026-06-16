import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. URL oficial actual de los planteles en Wikipedia
url = "https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_squads"

# 2. CONFIGURACIÓN CRÍTICA: Simular ser un navegador real para evitar el bloqueo
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("Conectando con Wikipedia...")
response = requests.get(url, headers=headers)

# 3. Pasar el contenido HTML usando el parser 'lxml' que es más robusto para tablas
soup = BeautifulSoup(response.content, 'lxml')

# 4. Wikipedia organiza los planteles en tablas con la clase 'wikitable'
tablas = soup.find_all('table', class_='wikitable')

print(f"Se encontraron {len(tablas)} tablas en la página. Extrayendo datos...")

lista_jugadores = []

# 5. Recorrer cada tabla encontrada
for index, tabla in enumerate(tablas):
    filas = tabla.find_all('tr')
    
    # Saltamos la primera fila (encabezados de la tabla)
    for fila in filas[1:]:
        celdas = fila.find_all(['td', 'th'])
        
        # Nos aseguramos de que sea una fila con la estructura correcta del jugador
        if len(celdas) >= 6:
            try:
                # Si la fila tiene el número de camiseta al inicio
                numero = celdas[0].text.strip()
                posicion = celdas[1].text.strip()
                nombre = celdas[2].text.strip()
                edad = celdas[3].text.strip()
                club = celdas[-1].text.strip() # El club suele ser la última celda
                
                lista_jugadores.append({
                    "Tabla_Index": index,
                    "Numero": numero,
                    "Posicion": posicion,
                    "Nombre": nombre,
                    "Edad_Fecha": edad,
                    "Club": club
                })
            except Exception as e:
                # Si alguna fila tiene un formato raro (como subtítulos internos), la salta sin romper el script
                continue

# 6. Guardar los resultados
if lista_jugadores:
    df = pd.DataFrame(lista_jugadores)
    df.to_csv("datos_crudos_mundial.csv", index=False)
    print(f"¡Éxito total! Se han raspado {len(df)} registros de jugadores.")
    print("Verifica tu archivo 'datos_crudos_mundial.csv' en la barra lateral.")
else:
    print("Alerta: Se volvieron a obtener 0 registros. Es posible que Wikipedia haya cambiado las etiquetas.")
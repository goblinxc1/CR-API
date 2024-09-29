import requests
import pandas as pd
import time 

# Definir la URL del clan y los headers para la solicitud API
clan_url = "https://api.clashroyale.com/v1/clans/%23YVRVCCYQ/members"
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFjMTYwMGRkLWI5ODUtNGE5Zi1hYjQ4LTAyMTE1YjZmYWE0NiIsImlhdCI6MTcyNzU4NjE3Nywic3ViIjoiZGV2ZWxvcGVyL2NlMjUwZWQwLTc2YzAtYmM5Mi1lZGMzLTg4ZTEyMGI0Y2U3NSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIzOC4xOTkuNy4yMTkiXSwidHlwZSI6ImNsaWVudCJ9XX0.amnDUiQiTdFMEocFOvSvlGGldv6nnUS0q5H3g6z3hIeFssHfcjzCAs3IcDygPZLshL_XwaFRerv-RuRZSGJjYw"  # Asegúrate de usar el token correcto
}

# Hacer la solicitud GET para obtener los miembros del clan
response = requests.get(clan_url, headers=headers)

if response.status_code == 200:
    clan_members = response.json().get("items", [])
    
    print("Ganadores de pass diamante y oro")
    
    count = 0
    top   = 0

    nombres_juga = []
    medallas_juga = []
    premios = ["Diamante", "Oro", "Oro", "Oro", "Oro"]

    # Iterar sobre los miembros para obtener sus medallas
    for member in clan_members:
        if count >= 5:  # Solo queremos los primeros 5
            break
        tag = member.get("tag").replace("#", "%23")  # Sanitizar el tag
        jugador_url = f"https://api.clashroyale.com/v1/players/{tag}"
        
        # Hacer la solicitud GET para obtener los datos de cada jugador
        jugador_response = requests.get(jugador_url, headers=headers)

        if jugador_response.status_code == 200:
            datos_jugador = jugador_response.json()
            current_season = datos_jugador.get("currentPathOfLegendSeasonResult", {})
            medallas = current_season.get("trophies", 0)
            nombre = datos_jugador.get("name", "Sin nombre")
            top += 1

            # Asignar el premio correspondiente
            premio_asignado = premios[count]

            print(f"{top}. {nombre} - Medallas: {medallas}- Premio: {premio_asignado}")
            #Guardar los datos en las listas
            nombres_juga.append(nombre)
            medallas_juga.append(medallas)
            count+=1
        else:
            print(f"Error al obtener datos del jugador {tag}: {jugador_response.status_code}")


    # #Guardar los nombres en un DataFrame
    # df = pd.DataFrame({
    #     "Nombre": nombres_juga,
    #     "Medallas": medallas_juga,
    #     "Premio": premios[:count]
    # }) 

    # guardar = f"top_ladder_{int(time.time())}.xlsx"
    # df.index = df.index +1
    # df.to_excel(guardar, index=True)
    
    # print(f"Guardado en: {guardar}")
else:
    print(f"Error al obtener los miembros del clan: {response.status_code}")
    print(response.text)

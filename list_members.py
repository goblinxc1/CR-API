import requests
import pandas as pd

# Definir la URL y los headers
url = "https://api.clashroyale.com/v1/clans/%23YVRVCCYQ/members"

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFjMTYwMGRkLWI5ODUtNGE5Zi1hYjQ4LTAyMTE1YjZmYWE0NiIsImlhdCI6MTcyNzU4NjE3Nywic3ViIjoiZGV2ZWxvcGVyL2NlMjUwZWQwLTc2YzAtYmM5Mi1lZGMzLTg4ZTEyMGI0Y2U3NSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIzOC4xOTkuNy4yMTkiXSwidHlwZSI6ImNsaWVudCJ9XX0.amnDUiQiTdFMEocFOvSvlGGldv6nnUS0q5H3g6z3hIeFssHfcjzCAs3IcDygPZLshL_XwaFRerv-RuRZSGJjYw"  # Asegúrate de usar el token correcto
}

# Hacer la solicitud GET
response = requests.get(url, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Extraer los datos de la respuesta JSON
    clan_members = response.json().get("items", [])
    
    # Mostrar los nombres de todos los miembros del clan
    print("Nombres de los miembros del clan:")
    
    # Crear una lista para almacenar los nombres
    member_names = []
    membre_trops = []
    contador = 0

    for member in clan_members:
        name = member.get("name")
        contador+=1
        print(f"{contador}. {name}")
        # member_names.append(name)  
        # membre_trops.append(trops)

    # # Guardar los nombres en un DataFrame
    # df = pd.DataFrame({
    #     "Nombre": member_names,
    #     "Copas": membre_trops
    # })

    # guardar = "data/1lista_miembros.xlsx"
    # df.index = df.index +1
    # df.to_excel(guardar, index=True)
    
    # print(f"Guardado en: {guardar}")
else:
    # Manejar el error
    print(f"Error {response.status_code}: {response.text}")

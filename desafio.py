import requests
import os
import json
lista_paises = []
def comprobar_nombre(nombre_pais):
    while nombre_pais == "":
        nombre_pais = (
            input("El nombre del pais no debe estar vacio, favor reintentar: ")
            .lower()
            .strip()
        )
    return nombre_pais


def consultar_pais(nombre_pais):
    url = f"https://restcountries.com/v3.1/name/{nombre_pais}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        info_pais = {
            "nombre": datos[0]["name"]["official"],
            "capital": datos[0]["capital"],
            "region": datos[0]["region"],
            "poblacion": datos[0]["population"],
            "idiomas": list(datos[0]["languages"].values()),
        }
        print(json.dumps(info_pais, indent=4, ensure_ascii=False))
        return info_pais

    elif respuesta.status_code == 404:
        print(f"Pais no encontrado {nombre_pais} no existe")
    return None


def guardar_info(informacion):
    ruta = "paises.json"
    datos_existentes = []
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos_existentes = json.load(archivo)
    datos_existentes.append(informacion)

    with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos_existentes, archivo, indent=4, ensure_ascii=False)


while True:
    pais = input("Ingrese el nombre de un pais: ").lower().strip()
    pais = comprobar_nombre(pais)

    informacion = consultar_pais(pais)
    lista_paises.append(informacion.get("nombre_oficial"))
    guardar_info(informacion)


    respuesta = input("Quieres consultar otro pais? (s/n): ").lower()

    if respuesta == "n":
        break

for pais in lista_paises:
    print(pais)
    with open('paises.json', 'r', encoding='utf-8') as archivo:
        todos_los_paises = json.load(archivo)
        for elem in todos_los_paises:
            if elem['nombre_oficial'] == pais:
                print(json.dumps(elem, indent=4, ensure_ascii=False))
                
        print("--------------------------------------------------")
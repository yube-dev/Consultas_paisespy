import requests


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
        print(datos[0].keys())
    elif respuesta.status_code == 404:
        print(f"Pais no encontrado {nombre_pais} no existe")


while True:
    pais = input("Ingrese el nombre de un pais: ").lower().strip()
    pais = comprobar_nombre(pais)

    consultar_pais(pais)

    respuesta = input("Quieres consultar otro pais? (s/n): ").lower()

    if respuesta == "n":
        break
# video 46:12, explicacion de la estructura de datos

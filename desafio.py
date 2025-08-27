import requests

def comprobar_nombre(nombre_pais):
    while nombre_pais == "":
        nombre_pais = (input('El nombre del pais no debe estar vacio, favor reintentar: ').lower().strip())
    return nombre_pais

def consultar_pais(nombre_pais):
    url = f"https://restcountries.com/v3.1/name/{nombre_pais}"



while True:
    pais = input("Ingrese el nombre de un pais: ").lower().strip() 
    pais = comprobar_nombre(pais)
    respuesta = input("Quieres consultar otro pais? (s/n): ").lower()

    if respuesta == "n":
        break

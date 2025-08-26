while True:
    pais = input("Ingrese el nombre de un pais: ").lower().strip() 

    respuesta = input("Quieres consultar otro pais? (s/n): ").lower()

    if respuesta == "n":
        break

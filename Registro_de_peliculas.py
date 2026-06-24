registro_de_peliculas = [
    { "titulo": "Oppenheimer", "duracion": 180, "calificacion": 8.5, "estado": "disponible"   },
    { "titulo": "Morbius", "duracion": 104, "calificacion": 5.2, "estado": "no disponible" },   ]
def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar pelicula")
    print("2. Buscar pelicula")
    print("3. Eliminar pelicula")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar peliculas")
    print("6. Salir")
def buscar_pelicula(lista, titulo):
    for i in range(len(lista)):
        if lista[i]["titulo"].lower() == titulo.lower():
            return i
    return -1
def actualizar_disponibilidad(lista):
    for pelicula in lista:
        pelicula["disponible"] = pelicula["calificacion"] >= 7.0
while True:
    mostrar_menu()
    opcion = input("Ingrese una opcion: ")
    while opcion not in ["1", "2", "3", "4", "5", "6"]:
        opcion = input("Opcion invalida. Ingrese nuevamente: ")
    if opcion == "1":
        titulo = input("Ingrese el titulo: ")
        if titulo.strip() == "":
            print("El titulo no puede estar vacio.")
            continue
        try:
            duracion = int(input("Ingrese la duracion: "))

            if duracion <= 0:
                print("La duracion debe ser mayor que 0.")
                continue
            calificacion = float(input("Ingrese la calificacion: "))
            if calificacion < 0 or calificacion > 10:
                print("La calificacion debe estar entre 0 y 10.")
                continue
        except ValueError:
            print("Error en los datos ingresados.")
            continue
        pelicula = {
            "titulo": titulo,
            "duracion": duracion,
            "calificacion": calificacion,
            "disponible": False
        }
        registro_de_peliculas.append(pelicula)
        print("Pelicula agregada.")
    elif opcion == "2":
        titulo = input("Ingrese la pelicula a buscar: ")
        posicion = buscar_pelicula(registro_de_peliculas, titulo)
        if posicion != -1:
            print("Pelicula encontrada:")
            print(registro_de_peliculas[posicion])
        else:
            print("Pelicula no encontrada.")
    elif opcion == "3":
        titulo = input("Ingrese la pelicula a eliminar: ")
        posicion = buscar_pelicula(registro_de_peliculas, titulo)
        if posicion != -1:
            registro_de_peliculas.pop(posicion)
            print("Pelicula eliminada.")
        else:
            print(f"La pelicula '{titulo}' no se encuentra registrada.")
    elif opcion == "4":
        actualizar_disponibilidad(registro_de_peliculas)
        print("Disponibilidad actualizada.")
    elif opcion == "5":
        actualizar_disponibilidad(registro_de_peliculas)
        print("\n=== LISTA DE PELICULAS ===")
        for pelicula in registro_de_peliculas:
            print("Titulo:", pelicula["titulo"])
            print("Duracion:", pelicula["duracion"])
            print("Calificacion:", pelicula["calificacion"])
            if pelicula["disponible"]:
                print("Estado: DISPONIBLE")
            else:
                print("Estado: NO RECOMENDADA")
            print("*" * 40)
    elif opcion == "6":
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
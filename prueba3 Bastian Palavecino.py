
datos_personales = []
boletas = []

cartelera = [
    ["spiderman lejos de casa", "15:00", 150, 2500],
    ["el rey leon", "16:30", 150, 2500],
    ["toy story 4", "17:20", 150, 2500],
    ["scream 4", "18:00", 150, 2500],
    ["super mario bros 2D", "19:00", 150, 2500],
    ["super mario bros 3D", "21:30", 150, 2500],
    ["avatar 3D", "21:30", 150, 2500]
]

filas_asientos = 15
columnas_asientos = 10
matriz_asientos = [["O" for _ in range(columnas_asientos)] for _ in range(filas_asientos)]

def registrar_datos():
    nombre = input("ingrese su nombre: ")
    correo = input("ingrese su correo: ")
    pregunta = int(input("¿usted es alumno duoc? [1] si [2] no: "))
    if pregunta == 1: 
        print("tiene un descuento por ser alumno 😜")
        datos_personales.append([nombre,  correo])
    else: 
        print("no tiene ningun descuento 😢 ")
    datos_personales.append([nombre, correo])

def mostrar_cartelera():
    print("cartelera disponible")
    for i, pelicula in enumerate(cartelera):
        print(i + 1, "-", pelicula[0], "- hora:", pelicula[1], "- asientos disponibles:", pelicula[2], "- precio:", pelicula[3])

def mostrar_matriz():
    print("mapa de asientos:")
    print("  ", end="")
    for i in range(1, columnas_asientos + 1):
        print(i, end=" ")
    print()
    for i in range(filas_asientos):
        print(chr(65 + i), end=" ")
        for j in range(columnas_asientos):
            print(matriz_asientos[i][j], end=" ")
        print()

def reservar_asientos():
    mostrar_cartelera()
    pelicula_index = int(input("seleccione una pelicula: ")) - 1
    if pelicula_index < 0 or pelicula_index >= len(cartelera):
        print("seleccione una pelicula que este disponible")
        return
    asientos_disponibles = cartelera[pelicula_index][2]
    if asientos_disponibles == 0:
        print("no quedan asientos disponibles para esta pelicula")
        return
    
    mostrar_matriz()
    print("seleccione los asientos (fila y columna) separados por comas (ejemplo: A1, B2, C3)")
    asientos_reservar = input("seleccione los asientos que desea reservar: ").split(", ")


    asientos_seleccionados = []
    for asiento in asientos_reservar:
        fila, columna = obtener_coordenadas_asiento(asiento)
        if not validar_asiento(fila, columna):
            print("el asiento", asiento, "no es valido")
            return
        if matriz_asientos[fila][columna] == "X":
            print("el asiento", asiento, "ya esta ocupado")
            return
        matriz_asientos[fila][columna] = "X"
        asientos_seleccionados.append(asiento)

    cartelera[pelicula_index][2] -= len(asientos_seleccionados)
    nombre = datos_personales[-1][0]
    correo = datos_personales[-1][2]
    pelicula = cartelera[pelicula_index][0]
    boleta = [nombre, correo, pelicula, len(asientos_seleccionados), asientos_seleccionados]
    boletas.append(boleta)
    generar_boleta(nombre, correo, pelicula, len(asientos_seleccionados), asientos_seleccionados)
    print("ha reservado sus asientos con exito")
    mostrar_matriz()

def obtener_coordenadas_asiento(asiento):
    fila = ord(asiento[0].upper()) - 65
    columna = int(asiento[1:]) - 1
    return fila, columna

def validar_asiento(fila, columna):
    return 0 <= fila < filas_asientos and 0 <= columna < columnas_asientos

def generar_boleta(nombre, correo, pelicula, asientos_reservados, asientos_seleccionados):
    print("-------boleta de reserva-------")
    print("nombre:", nombre)
    print("correo:", correo)
    print("pelicula:", pelicula)
    print("asientos reservados:", asientos_reservados)
    print("asientos seleccionados:", ", ".join(asientos_seleccionados))
    print("-------------------------------")

def mostrar_boletas():
    print("-------boletas generadas-------")
    for i, boleta in enumerate(boletas):
        nombre = boleta[0]
        correo = boleta[1]
        pelicula = boleta[2]
        asientos_reservados = boleta[3]
        asientos_seleccionados = boleta[4]
        generar_boleta(nombre, correo, pelicula, asientos_reservados, asientos_seleccionados)
    print("-------------------------------")


def menu():    
    registrar_datos()
    while True:
        print("seleccione una opcion:")
        print("1. mostrar cartelera")
        print("2. reservar asientos")
        print("3. mostrar boletas generadas")
        print("4. salir")

        opcion = input("seleccione una opcion: ")

        if opcion == "1":
            mostrar_cartelera()
        elif opcion == "2":
            reservar_asientos()
        elif opcion == "3":
            mostrar_boletas()
        elif opcion == "4":
            print("hasta la proxima")
            break
        else:
            print("opcion invalida por favor seleccione una opcion valida")
menu()


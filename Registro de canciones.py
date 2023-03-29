
"""
def InsertarCanciones(nombre,compositor,cantante, album, year):
    arreglo = []
    arreglo.append(nombre)
    arreglo.append(compositor)
    arreglo.append(cantante)
    arreglo.append(album)
    arreglo.append(year)
    return arreglo

def InsertarEnLista(cancion):
    lista = []
    lista.append(cancion)
    return lista

print('Declaramos el primer arreglo')

cancion = []
lista = []

print('Insertarmeos 4 canciones para una prueba')
for i in range (0,3):
    nombre = print('Ingrese nombre de cancion')
    compositor = print('Ingrese nombre de cancion')
    cantante = print('Ingrese nombre de cancion')
    album = print('Ingrese nombre de cancion')
    year = print('Ingrese nombre de cancion')
    cancion = InsertarCanciones(cancion,nombre,compositor,cantante,album,year)
    lista = InsertarEnLista(cancion)---
"""

# lista para almacenar las canciones
canciones = []

# agregamos las canciones
def agregar_cancion():
    nombre = input("Ingrese el nombre de la canción: ")
    compositor = input("Ingrese el nombre del compositor: ")
    cantante = input("Ingrese el nombre del cantante: ")
    album = input("Ingrese el nombre del álbum: ")
    year = input("Ingrese el año de la cancion: ")
    cancion = {
        "nombre": nombre,
        "compositor": compositor,
        "cantante": cantante,
        "album": album,
        "year": year
    }
    canciones.append(cancion)
    print("Canción agregada con éxito.")

##esta linea se agrega


# mostrar todas las canciones
def mostrar_canciones():
    if len(canciones) == 0:
        print("No se han registrado canciones.")
    else:
        for cancion in canciones:
            print(f'Cancion: {cancion["nombre"]}, Compositor: {cancion["compositor"]}, Cantante: {cancion["cantante"]}, Álbum: {cancion["album"]}')

# menu para agregar y mostrar las canciones
while True:
    print("1. Agregar una canción")
    print("2. Mostrar todas las canciones")
    print("3. Salir")
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        agregar_cancion()
    elif opcion == "2":
        mostrar_canciones()
    elif opcion == "3":
        print("Gracias por usar el programa. Hasta luego.")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
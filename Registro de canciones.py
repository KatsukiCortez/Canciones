#esta es la primera prueba de mi programa 
#iniciar un arreglo de informacion

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


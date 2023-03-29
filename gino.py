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
    print("Gino Cambio esta linea")


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

##################################################################


"""from tkinter import *
from tkinter import ttk
raiz = Tk()
raiz.title("Las Canciones")
raiz.geometry("520x480")
raiz.config(bg="green")
#Config Titulo
title = Label(raiz, text="Ingresa Tu Cancion")
title.pack(anchor=CENTER)
title.config(font=("Verdana",24))
title.place(x=110, y=10)
#Config SongName
songnametext = Label(raiz, text="Nombre de la Cancion: ")
songnametext.place(x=100, y=150)
songname = ttk.Entry()
songname.place(x=300, y=150)
#Config Compositor
compositorname = Label(raiz, text="Nombre del Compositor: ")
compositorname.place(x=100, y=200)
compositor = ttk.Entry()
compositor.place(x=300, y=200)
#Config Singer
singername = Label(raiz, text="Nombre del Cantante: ")
singername.place(x=100, y=250)
singer = ttk.Entry()
singer.place(x=300, y=250)
#Config Albun
albunname = Label(raiz, text="Nombre del Albun: ")
albunname.place(x=100, y=300)
albun = ttk.Entry()
albun.place(x=300, y=300)
#Config Year
yearname = Label(raiz, text="Año del Albun: ")
yearname.place(x=100, y=350)
year = ttk.Entry()
year.place(x=300, y=350)
#Boton de Confirmación
botonConfirmed = ttk.Button(text="Confirmar")
botonConfirmed.place(x=300, y=400)

raiz.mainloop()
"""

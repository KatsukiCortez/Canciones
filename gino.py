from tkinter import *
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
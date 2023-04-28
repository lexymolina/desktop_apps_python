#------------------------
# Desktop app No. 1
#------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *

#-----------------------
# funciones de la app
#-----------------------

#-----------------------------
# ventana principal de la app
#------------------------------

# se declara una variable llamada ventana principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title ("Bandera de noruega")

#tamaño de la ventana
ventana_principal.geometry("800x600")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la pantalla
ventana_principal.config(bg = "salmon1")

#---------------------------------
# frame rojo
#---------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg = "red3", width = 800, height = 600)
frame_rojo.place(x = 0, y = 0)

#---------------------------------
# frame blanca
#---------------------------------
frame_blanca = Frame(ventana_principal)
frame_blanca.config(bg = "white", width = 800, height = 20)
frame_blanca.place(x = 0, y = 280)

#---------------------------------
# frame blanca
#---------------------------------
frame_blanca = Frame(ventana_principal)
frame_blanca.config(bg = "white", width = 800, height = 20)
frame_blanca.place(x = 0, y = 350)

#---------------------------------
# frame blanca
#---------------------------------
frame_blanca = Frame(ventana_principal)
frame_blanca.config(bg = "white", width = 20, height = 600)
frame_blanca.place(x = 300, y = 0)

#---------------------------------
# frame blanca
#---------------------------------
frame_blanca = Frame(ventana_principal)
frame_blanca.config(bg = "white", width = 20, height = 600)
frame_blanca.place(x = 230, y = 0)

#---------------------------------
# frame azul
#---------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg = "navy", width = 800, height = 50)
frame_azul.place(x = 0, y = 300)

#---------------------------------
# frame azul
#---------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg = "navy", width = 50, height = 600)
frame_azul.place(x = 250, y = 0)

#run
ventana_principal.mainloop()
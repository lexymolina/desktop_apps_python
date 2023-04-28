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
ventana_principal.title ("Bandera de francia")

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
frame_rojo.config(bg = "red3", width = 800, height = 150)
frame_rojo.place(x = 0, y = 0)

#---------------------------------
# frame amarillo
#---------------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg = "yellow", width = 800, height = 300)
frame_amarillo.place(x = 0, y = 150)

#---------------------------------
# frame rojo
#---------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg = "red3", width = 800, height = 150)
frame_rojo.place(x = 0, y = 450)

#---------------------------------
# frame rojo
#---------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg = "red3", width = 100, height = 100)
frame_rojo.place(x = 100, y = 250)

#run
ventana_principal.mainloop()
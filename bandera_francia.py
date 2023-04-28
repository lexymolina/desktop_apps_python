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
ventana_principal.geometry("900x450")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la pantalla
ventana_principal.config(bg = "salmon1")

#---------------------------------
# frame amarillo
#---------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg = "navy", width = 300, height = 450)
frame_azul.place(x = 0, y = 0)

#---------------------------------
# frame azul
#---------------------------------
frame_blanca = Frame(ventana_principal)
frame_blanca.config(bg = "white", width = 300, height = 450)
frame_blanca.place(x = 300, y = 0)

#---------------------------------
# frame rojo
#---------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg = "red3", width = 300, height = 450)
frame_rojo.place(x = 600, y = 0)

#run
ventana_principal.mainloop()
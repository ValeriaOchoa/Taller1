## Ejemplo Aplicacion del tkinter
## Valeria Ochoa 
## Fecha: 19/Dic/2016

from tkinter import *

## Frase
def frase():
    print('\t\t\t Dos son mejores que uno;')
    print('\t    porque tienen una buena recompensa por su trabajo.')
    print('\t      Porque si caen, uno levantará a su compañero:')
    print('  pero que desgracia para aquel que no tiene a otro que lo ayude a levantar')
    print('\t\t\t Presione X para seguir')

widget = Button(None,text='Siguiente',command = frase)
widget.grid(row = 3,column = 2)


widget=Label(text="Ejemplo Tkinter \n Valeria Ochoa",
             font = "Cambria 25",
             fg = "White", ## color de letra
             bg = "Blue") ## color de fondo  
widget.grid(row=0,column=1)

widget.mainloop()

v = Tk()
v.title("Ejemplo \"tkinter\" VALERIA")
v.configure(bg = 'SkyBlue')

## frame dentro de la ventana
frame = Frame(v,relief = RIDGE,borderwidth=10)
frame.grid(row = 0, column = 0)

## etiquetas
et1 = Label(frame,
            text="VALERIA",
            font="Arial 40",
            fg="White",
            bg="Blue")

et1.grid(row=0)

## botones
boton = Button(text = "Salir",
               font = "Calibri 20 bold",
               fg="Black",
               bg="SkyBlue",
               command = v.destroy)
boton.grid(row=1)

## imagen
imagen=PhotoImage(file="amigo.gif")
label1 = Label(v,image=imagen)
label1.grid(row=0, column=1)
v.mainloop()

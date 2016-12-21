#NOMBRE:MICHAEL CARDENAS
#PROGRAMACION AVANZADA
#20/12/2016

import sys
from tkinter import*

master=Tk()
whatever_you_do="Bienvenido cierre la venatana del mensaje  e ingrese un numero"
msg=Message(master,text=whatever_you_do)
msg.config(bg='red',font=('times',18,'italic'))
msg.pack()
mainloop()

def hacer_click():
    try:
        a=int(entrada_texto.get())
        a=a*5
        etiqueta.config(text=a)
    except ValueError:
        etiqueta.config(text="introduzca el numero porfavor")
app=Tk()
app.title("MULTIPLICA EL NUMERO *5 ")
    
#Ventana Principal

vp = Frame(app)
vp.grid(column=0, row=0, padx=(80,80), pady=(30,30))
vp.columnconfigure(0, weight=5)
vp.rowconfigure(0, weight=5)
 
etiqueta = Label(vp,text="ingrese el Valor")
etiqueta.grid(column=2, row=2)
 
boton = Button(vp, text="Aceptar", command=hacer_click)
boton.grid(column=1, row=1)

boton2=Button(vp, text='Cerrar', command=vp.destroy)
boton2.grid(column=6, row=6)
 
valor = ""
entrada_texto = Entry(vp,textvariable=valor)
entrada_texto.grid(column=2, row=1)


 
app.mainloop()

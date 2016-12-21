#CALCULANDO OPERACIONES BASICAS

from tkinter import *
from tkinter import messagebox
from math import*
    
app = Tk()
app.title("OPERACIONES BASICAS")
app.geometry("600x200+200+200")
app.config(bg="pink")

def show_entry_fields():
    print("REALIZADO POR: %s" % (e1.get()))

#PIDIENDO NUMEROS PARA LAS OPERACIONES AL USUARIO
Label(app, text="NOMBRE:").grid(row=0)
e1 = Entry(app)
e1.grid(row=0, column=1)
e1.delete(0,20)

ope_label = Label(app,text="INGRESE NUMERO 1:")
ope_label.grid(row=1,column=1)
ope_str = StringVar()
ope_entry = Entry(app,textvariable=ope_str)
ope_entry.grid(row=1,column=2)

ope_label1 = Label(app,text="INGRESE NUMERO 2:")
ope_label1.grid(row=2,column=1)
ope_str1 = StringVar()
ope_entry1 = Entry(app,textvariable=ope_str1)
ope_entry1.grid(row=2,column=2)



#FUNCIONES A CALCULAR
def suma ():
	r=float(ope_entry.get())
	r1=float(ope_entry1.get()) 
	suma=r+r1
	messagebox.showinfo("resultados","LA SUMA ES: %.2f"%suma)
	ope_entry.delete(0,20)
	ope_entry1.delete(0,20)

def resta ():
	r=float(ope_entry.get())
	r1=float(ope_entry1.get()) 
	resta=r-r1
	messagebox.showinfo("resultados","LA RESTA ES: %.2f"%resta)
	ope_entry.delete(0,20)
	ope_entry1.delete(0,20)

def mult ():
	r=float(ope_entry.get())
	r1=float(ope_entry1.get()) 
	mult=r*r1
	messagebox.showinfo("resultados","LA MULTIPLICACION ES: %.2f"%mult)
	ope_entry.delete(0,20)
	ope_entry1.delete(0,20)


def div ():
	r=float(ope_entry.get())
	r1=float(ope_entry1.get()) 
	div=r/r1
	messagebox.showinfo("resultados","LA DIVISION ES: %.2f"%div)
	ope_entry.delete(0,20)
	ope_entry1.delete(0,20)


#CREANDO BOTONES
suma = Button(app, text = "CALCULAR SUMA", command = suma,width=25)
suma.grid(row=4,column=2)

resta = Button(app, text = "CALCULAR RESTA", command = resta, width=25)
resta.grid(row=4,column=3)	


mul = Button(app, text = "CALCULAR MULTIPLICACION", command = mult, width=25)
mul.grid(row=5,column=2)


div = Button(app, text = "CALCULAR DIVISION", command = div, width=25)
div.grid(row=5,column=3)

Button(app, text='Mostrar Nombre en consola',command=show_entry_fields,
width = 25).grid(row=0, column=3, sticky=W, pady=4)



app.mainloop()

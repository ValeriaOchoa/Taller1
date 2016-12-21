from tkinter import *
def suma():
    suma = float(entrada1.get()) + float(entrada2.get())
    Label(root,text=suma).place(x=70,y=120)
    
def resta():
    resta = float(entrada1.get()) - float(entrada2.get())
    labelr=Label(root,text=resta).place(x=70,y=120)
    
def multiplicacion():
    multiplicacion = float(entrada1.get()) * float(entrada2.get())
    Label(root,text=multiplicacion).place(x=70,y=120)
    
def division():
    division = float(entrada1.get()) / float(entrada2.get())
    labelr=Label(root,text=division).place(x=70,y=120)

root=Tk()
root.title("Operaciones basicas")
root.config(bg="black")
root.geometry("400x200")
root.resizable(width=FALSE, height=FALSE)

numero1 = IntVar()
numero2 = IntVar()
label=Label(root,text="Operaciones basicas").pack()
label1=Label(root,text="Ingrese un numero:").place(x=10,y=30)
entrada1 = Entry(root,textvariable=numero1)
entrada1.place(x=140,y=30)
label2=Label(root,text="Ingrese otro numero:").place(x=10,y=60)
entrada2 = Entry(root,textvariable=numero2)
entrada2.place(x=140,y=60)

suma = Button(root,text="Sumar",command=suma).place(x=10,y=90)
resta = Button(root,text="Restar",command=resta).place(x=70,y=90)
multiplicacion = Button(root,text="Multiplicar",command=multiplicacion).place(x=130,y=90)
division = Button(root,text="Division",command=division).place(x=220,y=90)

Button(root, text='Salir', command=root.destroy).place(x=120,y=150)

label1=Label(root,text="Resultado:").place(x=10,y=120)


root.mainloop()

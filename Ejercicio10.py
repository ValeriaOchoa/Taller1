from Tkinter import *
def show_entry_fields():
    print("Nombre: %s\nApellido: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master, text="Nombre:").grid(row=0)
Label(master, text="Apellido:").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Mostrar en consola', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
mainloop( )

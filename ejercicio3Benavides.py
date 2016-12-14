from tkinter import *
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="SALIR", fg="red",command=frame.quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(frame,text="ENTRAR",command=self.write_slogan)
        self.slogan.pack(side=LEFT)
    
    def write_slogan(self):
        print ("Estamos aprendiendo a usar Tkinter!")
root = Tk()
app = App(root)
root.mainloop()


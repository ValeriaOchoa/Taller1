##ESCUELA POLITECNICA NACIONAL
## DANILO BENAVIDES
##APLICACION tkinder
from tkinter import * 
import math
from matplotlib import pyplot

vtn=Tk()

# Función cuadrática.
def f1(x):
    a=1
    b=1
    c=1
    return (a*x*x)+(b*x)+c

# Función lineal.
def f2(x):
    a=1
    b=1
    return a*x + b

#Funcion Exponencial
def f3(x):
    a=2
    return a**x

# Funcion Logaritmica
def f4(x):
    if x<=0:
        return 0
    else:
        return math.log(x)
    
fun = Button(vtn,text="FUNCIONES",command=f1(1)).place(x=10,y=30)
Button(vtn, text='EXIT', command=vtn.destroy).place(x=20,y=70)
def main():
    # Valores del eje X que toma el gráfico.
    vtn=x = range(-5, 6)
    # Graficar de las 4 funciones
    vtn=pyplot.plot(x, [f1(i) for i in x])
    vtn=pyplot.plot(x, [f2(i) for i in x])
    vtn=pyplot.plot(x, [f3(i) for i in x])
    vtn=pyplot.plot(x, [f4(i) for i in x])

    # Establecer el color de los ejes
    vtn=pyplot.axhline(0, color="black")
    vtn=pyplot.axvline(0, color="black")
    # Limitar los valores de los ejes
    vtn=pyplot.xlim(-10, 10)
    vtn=pyplot.ylim(-10, 10)
    # Mostrarlo
    vtn=pyplot.show()

main()

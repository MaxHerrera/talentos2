from tkinter import *

flag=True

def arriba():
    lienzo.move(1, 0, -5)
    Tk.update(ventana)
def abajo():
    lienzo.move(1, 0, 5)
    Tk.update(ventana)
def izq():
    lienzo.move(1, -5, 0)
    Tk.update(ventana)
def der():
    lienzo.move(1, 5, 0)
    Tk.update(ventana)
def salir():
    global flag
    flag=False


ventana = Tk()
btn1=Button(ventana,text="Arriba", command=arriba)
btn2=Button(ventana,text="Abajo", command=abajo)
btn3=Button(ventana,text="Izquierda", command=izq)
btn4=Button(ventana,text="Derecha", command=der)
btn5=Button(ventana,text="Salir", command=salir)

lienzo = Canvas(ventana,width=400, height=400)
lienzo.pack()
lienzo.create_rectangle(190,190,210,210,fill='red')

Tk.update(ventana)

btn1.pack(side="top")
btn2.pack(side="bottom")
btn3.pack(side="left")
btn4.pack(side="right")
btn5.pack()

while(flag):
    Tk.update(ventana)

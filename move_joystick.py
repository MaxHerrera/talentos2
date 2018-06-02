import time
from tkinter import *
import serial


puerto = serial.Serial('/dev/tty.usbmodem1411')

ventana=Tk()
lienzo=Canvas(ventana,width=500,height=500)

lienzo.pack()
lienzo.create_rectangle(200,350,300,450,fill='red')
Tk.update(ventana)
time.sleep(3)

x="0"
y="0"

while True:

    datos = str(serial.Serial.readline(puerto))
    print(datos)
    if int(datos.find("X: ")) == 2:
        x = (datos[5:datos.find("\r\n'")-4])
        print(x)
    if int(datos.find("Y: ")) == 2:
        y = (datos[5:datos.find("\r\n'")-4])
        print(y)

'''
    if mov=="arriba":
        lienzo.move(1,0,-2)
        Tk.update(ventana)
        time.sleep(0.1)

    if mov=="abajo":
        lienzo.move(1,0,2)
        Tk.update(ventana)
        time.sleep(0.1)

    if mov=="izquierda":
        lienzo.move(1,-2,0)
        Tk.update(ventana)
        time.sleep(0.1)
    if mov=="derecha":
        lienzo.move(1,2,0)
        Tk.update(ventana)
        time.sleep(0.1)
'''

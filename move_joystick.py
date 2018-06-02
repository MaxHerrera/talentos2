import time
from tkinter import *
import serial


puerto = serial.Serial('/dev/tty.usbmodem1411')

ventana=Tk()
lienzo=Canvas(ventana,width=1000,height=1000)

lienzo.pack()
lienzo.create_rectangle(400,400,450,450,fill='red')
Tk.update(ventana)
time.sleep(3)

x="0"
y="0"

while True:

    serial.Serial.flushInput(puerto)
    datos = str(serial.Serial.readline(puerto))
    print(datos)
    if int(datos.find("X: ")) == 2:
        x = (datos[5:datos.find("\r\n'")-4])
        print(x)
    if int(datos.find("Y: ")) == 2:
        y = (datos[5:datos.find("\r\n'")-4])
        print(y)


    if int(x)<543 and int(x)!=0 :
        lienzo.move(1,-(543-int(x)),0)
        Tk.update(ventana)
        time.sleep(0.25)

    if int(x)>543 and int(x)!=0:
        lienzo.move(1,(int(x)-543), 0)
        Tk.update(ventana)
        time.sleep(0.25)

    if int(y) < 564 and int(y)!=0:
        lienzo.move(1,0, -(564 - int(y)))
        Tk.update(ventana)
        time.sleep(0.25)
        
    if int(y) > 564 and int(y)!=0:
        lienzo.move(1,0, (int(y) - 564))
        Tk.update(ventana)
        time.sleep(0.25)




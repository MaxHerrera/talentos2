import serial

puerto = serial.Serial('/dev/tty.usbmodem14231')
while(True):
    datos = str(serial.Serial.readline(puerto))
    print(datos)



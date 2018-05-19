import serial

puerto = serial.Serial('/dev/tty.usbmodem')
while(True):
    datos = str(serial.Serial.readline(puerto))
    print(datos)



#-*- coding:utf-8 -*-
#!/usr/bin/python

# Se importan las librerias serial y time

import serial, time

# Se establece el puerto por el cual ingresa la información al pc
# Mismo puerto configurado en el arduino IDE
port = serial.Serial('/dev/ttyACM0',9600)

# Loop infinito, mientras ingrese información al pc estará funcionando
while True:
    # Leemos la linea que se envía desde el arduino
    port_message = port.readline()
    print port_message.rstrip('\n')

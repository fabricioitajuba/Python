# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#27/11/2020
#Recebendo dados pela serial usando threading (modo daemon)
#para executar: $ python main.py

import sys
import threading
import serial
import time

try:
	ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
except:
	print("Placa não conectada")
	sys.exit() #Sai do programa

time.sleep(3)
numPoints = 100
dataList = [0]*numPoints

def getValues():
	ser.write(b'g')
	arduinoData = ser.readline().decode().split('\r\n') #int
	return arduinoData[0]

def thread():
	for i in range(0, numPoints):
		data = getValues()
		data = int(data)
		dataList[i] = data
 
#Cria a thread
t = threading.Thread(target=thread, daemon=True)

#Starta a thread
t.start()

#Aguardando a thread ser executada 
while t.is_alive():
    print("Aguardando thread")
    time.sleep(1)
 
print(dataList)
print(dataList[0])

ser.close()

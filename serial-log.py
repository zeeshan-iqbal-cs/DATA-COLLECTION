import serial
import sys
import time
import os

print('************************************************************')
print('*  A pthon code written for Air Quality Sensor Calibration *')
print('*        It will Read data from USB port and               *')
print('*      Display on Screen and Same on File as named         *')
print('*            as Sensor id                                  *')
print('************************************************************')

serial_port = input('ENTER Serial-Port:')
sensor_id = input('Enter Sensor-ID:')

f = open(sensor_id + ".csv", "a+")

ser = serial.Serial()
ser.baudrate = 9600
ser.port = serial_port
ser.open()

while True:
    data = ser.readline()
    data = data.decode('ascii')
    data = data.replace('\r\n', '')
    data = str(time.time()) + "," + data
    print(data)
    f.write(data + "\n")

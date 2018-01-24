import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600)

while True:
    time.sleep(1)
    data = arduino.readline()
    d = int(data.decode('UTF','ignore'))
    print('Distancia: %i' % d)

arduino.close()

#cut and paste from StackExchange using pySerial

import time
import serial


#Establish connection on the port

ser = serial.Serial('/dev/ttyACM0', 9600)


x = 1
while x==1:
	out = ser.read(20)
	if out == ("TILT: X AXIS"):
		print ("Oh shit")
#	else:
#		print ser.readline()
	time.sleep(1)
	print(out)

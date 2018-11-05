import time
import serial

x = 1

while x == 1:

	ser = serial.Serial('/dev/ttyACM0', 9600)
	print("connection")

	out = ser.readline()
	read = str(out)
	print("out read")

	if read in ["TILT: X AXIS\n"]:
		print("x axis tilting :)")
	elif read in ["TILT: Y AXIS\n"]:
		print("y axis tilting :(")
	else:
		print("reading: ", read)

	print("end of while")
	time.sleep(1)



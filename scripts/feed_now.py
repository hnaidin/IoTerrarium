import serial
import time
ser = serial.Serial('/dev/ttyACM0' , 9600)
ser.write(chr(1))

while 1:
    str = ser.readline()
    print "Received %s"%str
    if str == "Done feeding":
        sys.exit(0)
    time.sleep(0.5)

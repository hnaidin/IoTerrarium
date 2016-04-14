#/usr/bin/python
import sys
import serial
import argparse

class TemperatureGetter:
    def __init__(self):
    	ser = serial.Serial('/dev/ttyACM0' , 9600)
    def getTemp():
        ser.write("0")
        while not str:
            str = ser.readline()
        print str
	ser.close()
	return str

class TurtleFeeder:
    def __init__(self):    
	ser = serial.Serial('/dev/ttyACM0' , 9600)
    def feed():
        ser.write("1")
	ser.close()

def main(argv):
    parser = argparse.ArgumentParser(description='Terrarium control script')
    parser.add_argument('-f','--feed', help='Feed the turtles [1 for True]', required=False)
    parser.add_argument('-t','--temp', help='Get the temperature from the sensor [1 for True]', required=False)
    args = vars(parser.parse_args())

    if args['feed'] == '1':
	t = TurtleFeeder()
	t.feed()

    if args['temp'] == '1':
        t = TemperatureGetter()
        temp = t.getTemp()
    pass

if __name__ == "__main__":
    main(sys.argv)


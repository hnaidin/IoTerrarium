import serial

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

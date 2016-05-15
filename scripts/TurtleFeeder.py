import serial

class TurtleFeeder:
    def __init__(self):
        ser = serial.Serial('/dev/ttyACM0' , 9600)
    def feed():
        ser.write("1")
        ser.close()

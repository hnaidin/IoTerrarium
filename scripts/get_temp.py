#/usr/bin/python
import sys
import argparse
import TurtleFeeder
import TemperatureGetter

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


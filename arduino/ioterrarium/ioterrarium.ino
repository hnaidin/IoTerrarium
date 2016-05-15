#include <Servo.h>

// Const definitions
#define GET_TEMP 0
#define FEED_TURTLES 1

// Servo variables
Servo myservo;  // create servo object to control a servo
int pos = 0;    // variable to store the servo position

// Serial line variables
int incomingByte = 0;   // for incoming serial data

void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
        myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {

        // send data only when you receive data:
        if (Serial.available() > 0) {
                // read the incoming byte:
                incomingByte = Serial.read();

                // say what you got:
                Serial.print("I received: ");
                Serial.println(incomingByte, DEC);
                
                switch(incomingByte){
                  case GET_TEMP:
                    break;
                  case FEED_TURTLES:
                    Serial.println("Feeding turtles... ");
                    myservo.write(150);
                    delay(2000);
                    myservo.write(0);
                    delay(2000);
                    
                    Serial.println("Done feeding");
                    break;
                  default:
                    Serial.println("CMD Error");
                    break;
                }
        }
}


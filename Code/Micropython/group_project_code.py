from machine import Pin
from states_group import idle, forward, left, right
import utime

#defining state checks
IDLE = "idle"
FORWARD = "forward"
TURN_LEFT = "left"
TURN_RIGHT = "right"

currentState = IDLE

TCRT1 = Pin(26, Pin.ANALOG)
TCRT2 = Pin(27, Pin.ANALOG)
TCRT3 = Pin(28, Pin.ANALOG)

#define motor input pins
input1 = Pin(0, Pin.OUT)
input2 = Pin(1, Pin.OUT)
input3 = Pin(2, Pin.OUT)
input4 = Pin(3, Pin.OUT)

#set all motors low
input1.low()
input2.low()
input3.low()
input4.low()
utime.sleep(1)

while True:
    if(TCRT3 < 100):
        #front wall detected
        currentState = IDLE
        if(TCRT1 > TCRT2):
            #turn to the left
            currentState = LEFT
        else:
            #turn to the right
            currentState = RIGHT
    else:
        #go forward
        currentState = FORWARD
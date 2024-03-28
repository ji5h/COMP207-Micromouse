from machine import Pin, PWM
from laser_sensing import tofL, tofR, tofF
from data_read import cardRegistered
from states import idle, forward, leftTurn, rightTurn, turnAround
import utime

#defining state checks
IDLE = "idle"
FORWARD = "forward"
TURN_LEFT = "turn left"
TURN_RIGHT = "turn right"
TURN_AROUND = "turn around"

currentState = IDLE

#defining transitions
FRONT_WALL = "front wall detected"
RIGHT_WALL = "right wall detected"
LEFT_WALL = "left wall detected"
ALL_WALL = "all wall detected"



buzzer = PWM(Pin(14,Pin.OUT))
buzzer.duty_u16(0)

#define motor input pins
input1 = Pin(0, Pin.OUT)
input2 = Pin(1, Pin.OUT)
input3 = Pin(2, Pin.OUT)
input4 = Pin(3, Pin.OUT)

input1.low()
input2.low()
input3.low()
input4.low()
utime.sleep(1)

tofL.start()
tofR.start()
tofF.start()
        
while cardRegistered:
    distanceL = tofL.read()
    distanceR = tofR.read()
    distanceF = tofF.read()
    print(currentState)
    
    if (currentState == IDLE):
        idle()
    elif (currentState == FORWARD):
        forward()
    elif (currentState == TURN_LEFT):
        leftTurn()
    elif (currentState == TURN_RIGHT):
        rightTurn()
    elif (currentState == TURN_AROUND):
        turnAround()
    
    if (distanceR < 100):
        if (distanceF > 100):
            currentState = FORWARD
        elif (distanceL > 100):
            currentState = TURN_LEFT
    else:
        currentState = TURN_RIGHT
        


    
tofL.stop()
tofR.stop()
tofF.stop()


    
from machine import Pin, PWM
from laser_sensing import tofL, tofR, tofF
from data_read import cardRegistered
from states import idle, forward, leftTurn, rightTurn, turnAround
import utime


#define motor input pins 
input1 = PWM(Pin(0))
input1.freq(1000)
input2 = Pin(1, Pin.OUT)
input3 = Pin(2, Pin.OUT)
input4 = PWM(Pin(3))
input4.freq(1000)


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
    
    input1.duty_u16(distanceL*10)
    input2.low()
    
    input3.low()
    input4.duty_u16(distanceR*10)


    
tofL.stop()
tofR.stop()
tofF.stop()

from machine import Pin, PWM
import utime

#define motor input pins
input1 = Pin(0, Pin.OUT)
input2 = Pin(1, Pin.OUT)
input3 = Pin(2, Pin.OUT)
input4 = Pin(3, Pin.OUT)

def idle():
    input1.low()
    input2.low()
    input3.low()
    input4.low()

def forward():
    input1.high()
    input2.low()
    input3.low()
    input4.high()

def leftTurn():
    input1.low()
    input2.high()
    input3.low()
    input4.high()
    
def rightTurn():
    input1.high()
    input2.low()
    input3.high()
    input4.low()

def turnAround():
    input1.low()
    input2.low()
    input3.high()
    input4.low()
    utime.sleep(1)

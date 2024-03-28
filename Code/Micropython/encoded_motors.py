from machine import Pin, PWM
import time

input3 = Pin(2, Pin.OUT)
input2 = Pin(3, Pin.OUT)

enA = Pin(12, Pin.IN)
enB = Pin(13, Pin.IN)

pos = 0

def readEnc(p):
    global pos
    if enB.value():
        pos += 1
    else:
        pos -= 1

enA.irq(trigger=Pin.IRQ_RISING, handler=readEnc)

while True:
    state = machine.disable_irq()
    machine.enable_irq(state)
    input1.high()
    input2.low()
    time.sleep(1)
    print(pos)
    input1.low()
    input2.high()
    time.sleep(1)
    print(pos)
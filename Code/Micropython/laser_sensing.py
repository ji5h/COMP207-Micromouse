from machine import Pin
from machine import I2C
from vl53l0x import VL53L0X

I2C_bus = I2C(0, sda=Pin(8), scl=Pin(9))

xShutPinL = 26
xShutPinR = 27
xShutPinF = 28

defaultAddress = 0x29

#--------INITIALISE XSHUT PINS--------
xShutL = Pin(xShutPinL, Pin.OUT)
xShutR = Pin(xShutPinR, Pin.OUT)
xShutF = Pin(xShutPinF, Pin.OUT)

xShutL.low()
xShutR.low()
xShutF.low()

#--------CHANGE ADRESS OF LEFT SENSOR--------
#trying to overide default address of i2c
xShutL.high()

# read value from 0x16,0x17
high = I2C_bus.readfrom(defaultAddress, 0x16)
low = I2C_bus.readfrom(defaultAddress, 0x17)

# write value to 0x18,0x19
I2C_bus.writeto_mem(defaultAddress, 0x18, high)
I2C_bus.writeto_mem(defaultAddress, 0x19, low)

# write new_address to 0x8a
I2C_bus.writeto_mem(defaultAddress, 0x8a, bytes([0x30]))

#initialise the tof left sensor
tofL = VL53L0X(I2C_bus,address=0x30)
#--------CHANGE ADDRESS OF RIGHT SENSOR--------
xShutR.high()
devices = I2C_bus.scan()
# write value to 0x18,0x19
I2C_bus.writeto_mem(defaultAddress, 0x18, high)
I2C_bus.writeto_mem(defaultAddress, 0x19, low)

# write new_address to 0x8a
I2C_bus.writeto_mem(defaultAddress, 0x8a, bytes([0x31]))

#initialise the tof left sensor
tofR = VL53L0X(I2C_bus,address=0x31)

#--------CHANGE ADDRESS OF FRONT SENSOR--------
xShutF.high()
#initialise the tof left sensor
tofF = VL53L0X(I2C_bus,address=0x29)



devices = I2C_bus.scan()
print(len(devices))
for device in devices:
 print("i2C Address: ",hex(device))

    



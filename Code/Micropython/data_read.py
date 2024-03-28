from mfrc522 import MFRC522
import utime
from machine import Pin
from machine import PWM
import random
 
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)

buzzer = PWM(Pin(14,Pin.OUT))
buzzer.duty_u16(0)
 
print("Show me that fucker it ain't close enough bitch")
print("")
 
 
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            if (card == 3238762580):
                print("CARD ID: "+str(card))
                buzzer.freq(random.randint(10,1000))
                buzzer.duty_u16(32000)
                utime.sleep_ms(500)
                buzzer.freq(1000)
                buzzer.duty_u16(0)
            elif (card == 972552362):
                print("fuck off will")
            elif (card == 3307243962):
                print("hi ben can u give me a good grade please")
            elif (card == 2014232486):
                print("fuck off james")
            else:
                print("Wrong card bitch can't access my shit")
                print("CARD ID: "+str(card))

utime.sleep_ms(500)
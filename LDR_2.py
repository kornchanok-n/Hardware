from machine import Pin,ADC
from time import sleep

LDR = 32
ldr = ADC(Pin(LDR))

#LDR = 19
#ldr = Pin(LDR,Pin.IN)
#''change read to value''

while(1):
  print(ldr.read())
  sleep(0.5)

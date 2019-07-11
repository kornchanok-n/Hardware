from machine import Pin, ADC
from time import sleep

led = Pin(5,Pin.OUT)

ldr = ADC(Pin(34))

while(1) :
  val = ldr.read()
  print(val)
  sleep(0.1)
  if val <= 3000:
    led.value(0)
  else:
    led.value(1)



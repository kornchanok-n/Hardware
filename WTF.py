from machine import Pin
from time import sleep

LED = Pin(5,Pin.OUT)
state = 0

while(1):
  if(state==0):
    LED.value(1)
    state = 1
  else:
    LED.value(0)
    state = 0
  sleep(2)

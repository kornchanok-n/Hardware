from machine import Pin
from time import sleep

led = Pin(5,Pin.OUT)

while(True):
  led.value(0)
  sleep(0.5)
  led.value(1)
  sleep(0.5)

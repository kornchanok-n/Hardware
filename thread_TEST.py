from machine import Pin,DAC,PWM
from time import sleep
from _thread import start_new_thread as thread


led1 =  Pin(5,Pin.OUT)
led2 =  Pin(12,Pin.OUT)

def showLed1():
  while(1):
    led1.value(not led1.value())
    sleep(0.5)
  
def showLed2(delay):
  while(1):
    led2.value(not led2.value())
    sleep(delay)


thread(showLed1,())
thread(showLed2,[0.2])


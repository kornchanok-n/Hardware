from machine import Pin,DAC,PWM
from time import sleep

buzzer = PWM(Pin(25))
i=0

while(1):
  buzzer.freq(10)
  sleep(0.5)
  buzzer.deinit()









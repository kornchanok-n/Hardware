from machine import Pin
from time import sleep

R=Pin(21,Pin.OUT)
G=Pin(19,Pin.OUT)
B=Pin(18,Pin.OUT)

while(1):
  R.value(1)
  G.value(0)
  B.value(0)
  sleep(0.5)
  
  R.value(1)
  G.value(1)
  B.value(0)
  sleep(0.5)
  
  R.value(0)
  G.value(1)
  B.value(0)
  sleep(0.5)
  
  R.value(0)
  G.value(1)
  B.value(1)
  sleep(0.5)
  
  R.value(0)
  G.value(0)
  B.value(1)
  sleep(0.5)
  
  R.value(1)
  G.value(0)
  B.value(1)
  sleep(0.5)
  
  
  

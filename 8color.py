from machine import Pin
from time import sleep
from _thread import start_new_thread as thread

R=Pin(21,Pin.OUT)
G=Pin(19,Pin.OUT)
B=Pin(18,Pin.OUT)

switch=Pin(25,Pin.IN)

count=0

def push():
  global count
  count=0
  while(1):
    if switch.value()==0:
      while switch.value()==0:
        if switch.value()==1:
          break
      count += 1
      sleep(0.5)
      print(count)

def blink(r,g,b):
  while(switch.value()==1):
    R.value(r)
    G.value(g)
    B.value(b)
    sleep(0.05)
    R.value(0)
    G.value(0)
    B.value(0)
    sleep(0.05)

def light():
  while(1):
    if count == 0 or count%8 ==0 :
      blink(1,0,0)
    else:   
      if count%8 == 1:
        blink(0,1,0)
      if count%8 == 2:
        blink(0,0,1)
      if count%8 == 3:
        blink(1,1,0)
      if count%8 == 4:
        blink(1,0,1)
      if count%8 == 5:
        blink(0,1,1)
      if count%8 == 6:
        blink(1,1,1)
      if count%8 == 7:
        blink(0,0,0)

thread(push,())
thread(light,())


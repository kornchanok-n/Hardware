from machine import Pin,PWM,ADC,DAC
from time import sleep
from _thread import start_new_thread as thread
import json,network,urequests

ssid='exceed16_8'
pwd='12345678'
station=network.WLAN(network.STA_IF)
station.active(True)

statBuzzer = 'off'
statDoor = 'close'


infra = Pin(26, Pin.OUT)
ldr = ADC(Pin(32))
R = Pin(21, Pin.OUT)
G = Pin(19, Pin.OUT)
B = Pin(18, Pin.OUT)
SW = Pin(27, Pin.IN)
switch1=Pin(25,Pin.IN)
servo = PWM(Pin(22),freq=50,duty=77)
count=0


def door():
  global servo
  global statDoor
  statDoor='close'
  servo.duty(120)
  sleep(0.5)
  global count
  count=0
  while(1):
    if switch1.value()==0:
      count+=1
      print(switch1.value())
      #print(count)
      if count%2 == 0 :#or statDoor=='close':
        servo.duty(120)
        #print(switch1.value())
        sleep(1)
        statDoor='close'     
      elif count%2 == 1 :#or statDoor=='open':
        servo.duty(65)
        sleep(1)
        statDoor='open' 
    sleep(0.5)

def laser():
  global statBuzzer
  #statBuzzer = 'off'
  while(1):
    infra.value(1)
    sleep(2)
    if ldr.read() > 4000 and infra.value() == 1:
      while(1):
        buzzer = PWM(Pin(2))
        buzzer.freq(20)
        #statBuzzer = 'on'
        R.value(1)
        G.value(0)
        B.value(0)
        sleep(0.5)
        R.value(0)
        G.value(0)
        B.value(1)
        sleep(0.5)
        #print(SW.value())
        if SW.value()==0 or count%2==1:
          buzzer.deinit()
          #statBuzzer = 'off'
          R.value(0)
          G.value(0)
          B.value(0)   
          break  
      sleep(0.2)
    if SW.value()==0 or count%2==1:
      infra.value(0)
      break
  
def onofflight():
  SWon = False
  while(1):
    buzzer = PWM(Pin(2))
    if SW.value() == 0 and SWon == False:
      SWon = True
      while(1):
        buzzer.freq(20)
        R.value(1)
        G.value(0)
        B.value(0)
        sleep(0.5)
        R.value(0)
        G.value(0)
        B.value(1)
        sleep(0.5)
        
        if SW.value() == 0:
          break
    
    buzzer.deinit()
    R.value(0)
    G.value(0)
    B.value(0)
    SWon = False


def onofflaser():
  while(1):
    if count%2 == 0 :
      laser()
    sleep(0.5)
 
 
def mynetwork():
  while(1):
    url = 'https://exceed.superposition.pknn.dev/data/eight'
    data = {"door":statDoor,"buzzer":statBuzzer}
    headers = {'content-type':'application/json'}
    while not station.isconnected():
      station.connect(ssid,pwd)
      print('Connecting ...')
      sleep(1)
      if station.isconnected():
        print('Connected')

    js = json.dumps({'data':data})
    r = urequests.post(url,data=js,headers=headers)
    results = r.json()
    print(results)
    
    r = urequests.get(url).json()
    print(r)
    sleep(1)
    
thread(door,())
thread(onofflaser,())
thread(mynetwork,())
#thread(onofflight,())




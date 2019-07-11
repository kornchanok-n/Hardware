import network
from time import sleep

ssid='exceed16_8'
pwd='12345678'
station=network.WLAN(network.STA_IF)
station.active(True)
print(station.isconnected())

while(1):
  while not station.isconnected():
    station.connect(ssid,pwd)
    print('Connecting ...')
    sleep(1)
    if station.isconnected():
      print('Connected')
  sleep(2)

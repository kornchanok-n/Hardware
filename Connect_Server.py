import json,network,urequests
from time import sleep

ssid='exceed16_8'
pwd='12345678'
station=network.WLAN(network.STA_IF)
station.active(True)

url = 'https://exceed.superposition.pknn.dev/data/8'
data = {'temp':34,'humid':12}
headers = {'content-type':'application/json'}

while(1):
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
  
  ###for get #
  r = urequests.get(url).json()
  print(r)
  sleep(4)
  


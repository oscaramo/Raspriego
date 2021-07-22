import Adafruit_DHT
sensor=Adafruit_DHT.DHT11
DHT11_pin=4

hum,temp=Adafruit_DHT.read_retry(sensor,DHT11_pin)
if hum is not None and temp is not None:
    print("Temp:"+str(temp)+", Hum:"+str(hum))

else:
    print("Failed to reading from the sensor")

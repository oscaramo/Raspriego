import Adafruit_DHT
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

#Set the ADC gain to 2
ads.gain=2



#Creating a DHT11 sensor object

sensor=Adafruit_DHT.DHT11
DHT11_pin=4

#Creating a txt file to write the data
f=open("value.txt","w")
f.write("Temp    Hum    Light \n")

h=0
m=0

#Bucle infinit
while True:
    if h<19:    #Nombre d'hores que volem prendre dades
       #Escriure les dades al fitxer 
       hum,temp=Adafruit_DHT.read_retry(sensor,DHT11_pin)
       V=chan.voltage
       v=str(V)[0:4]
       f.write(str(temp)+"    "+str(hum)+"    "+str(v)+"\n")
       #Prendre dades cada t minuts
       t=5
       time.sleep(60*t)
       m=m+t
       if m>=60:
           m=0
           h=h+1
    else:
        break
    

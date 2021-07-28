import Adafruit_DHT
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
from datetime import date


data=[] #Dades d'un dia
data_m=[] #Dades mitjanes d'un dia

#Config GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT) #Pin control bomba

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

#Set the ADC gain to 2
ads.gain=1

#Creating a DHT11 sensor object
sensor=Adafruit_DHT.DHT11
DHT11_pin=4

def mean(l):
    t=0
    h=0
    v=0
    n=0
    for i in l:
        n=n+1
        t=t+i[0]
        h=h+i[1]
        v=v+i[2]
    return([t/n,h/n,v/n])

m=0.5 #minuts d'espera de cada cicle
#day=date.today().day
n=0
while True:
    n=n+1
    #if day=date.today().day:
    if n<=2:
        #si no canvia va guardant les dades al dataframe i encen bomba si la
        #llum baixa
        hum,temp=Adafruit_DHT.read_retry(sensor,DHT11_pin)
        V=chan.voltage
        V=float(str(V)[0:4])
        data.append([temp,hum,V])

        #Condicions de reg (de moment amb fotoresistor,
        #per a poder veure que funciona)
        if V>=2.0:
            GPIO.output(17,True)
            time.sleep(10)
            GPIO.output(17,False)
        else:
            GPIO.output(17,False)
        #day=date.today().day
        time.sleep(60*m)

    else:
        #Guarda les dades mitjanes de cada dia, per a poder configurar les
        #condicions de reg
        print(data)
        data_m.append(mean(data))    
        data=[]
        print(data_m)
        break

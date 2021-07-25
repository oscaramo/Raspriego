import Adafruit_DHT
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
import pandas as pd
from datetime import date


#Dataframe to save the values of a day
data={"Temp":[],"Hum":[],"Light":[]}
df=pd.DataFrame(data)
df_m=pd.DataFrame(data)

#Funcio per a afegir dades al DF
def add_v(df,T,H,L):
    df2={"Temp":[T],"Hum":[H],"Light":[L]}
    df2=pd.DataFrame(df2)
    df=df.append(df2)
    return df


#Config GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT) #Pin control bomba

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

m=1 #minuts d'espera de cada cicle
day=date.today().day

while True:
    if day=date.today().day:
        #si no canvia va guardant les dades al dataframe i encen bomba si la
        #llum baixa
        hum,temp=Adafruit_DHT.read_retry(sensor,DHT11_pin)
        V=chan.voltage
        V=float(str(V)[0:4])
        df=add_v(df,temp,hum,v)

        #Condicions de reg (de moment amb fotoresistor,
        #per a poder veure que funciona)
        if V>=1:#
            GPIO.output(7,True)
            time.sleep(10)
        else:
            GPIO.output(7,False)
        day=date.today().day
        time.sleep(60*m)

    else:
        #Guarda les dades mitjanes de cada dia, per a poder configurar les
        #condicions de reg
        T=df["Temp"].mean()
        H=df["Hum"].mean()
        L=df["Hum"].mean()
        df_m=add_v(df_m,T,H,L)
        #df=pd.DataFrame(data)
        #df.to_csv()
        break

import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import math


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

#Create a Document to write data
f=open("Temperatures","w")

f.write("Temp Voltage \n")
ads.gain=2
R1=10000
A=0.001129148
B=0.000234125
C=0.0000000876741

def temp(v,r,A,B,C):
    Rntc=r*v/(3.3-v)
    logRntc=math.log10(Rntc)
    Tk=1/(A+B*logRntc+C*logRntc*logRntc
    TC=Tk-273.15
    return(TC)
    
n=1
while n<10:
    #T=chan.value
    V=chan.voltage
    Tc=temp(V,R1,A,B,C)
    f.write(+str(Tc)+" "+str(V)+"\n")
    time.sleep(5)
    n=n+1

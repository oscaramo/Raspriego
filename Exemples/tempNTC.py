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

f.write("Temp Voltage Resistance \n")
ads.gain=2
R1=1000
b=3600
a=1.7719

def temp(r,v,a,b):
    Rntc=r*v/(3.3-v)
    log=math.log(Rntc,a)
    Tk=b/log
    TC=Tk-273.15
    return([TC,Rntc])
#A=2.229674985*(10^-3)
#B=1.211871252*(10^-4)
#C=8.713435086*(10^-7)

#def temp(v,r,A,B,C):
 #   Rntc=r*v/(3.3-v)
  #  logRntc=math.log10(Rntc)
   # Tk=1/(A+B*logRntc+C*logRntc*logRntc)
    #TC=Tk-273.15
    #return([TC,Rntc])
    
n=1
while n<10:
    #T=chan.value
    V=chan.voltage
    l=temp(R1,V,a,b)
    Tc=l[0]
    Rntc=l[1]
    f.write(str(Tc)+" "+str(V)+" "+str(Rntc)+"\n")
    time.sleep(5)
    n=n+1

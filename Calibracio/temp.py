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

#Create a Document to write data
f=open("Temperatures","w")

f.write("Time Temp Voltage")
ads.gain=2

#int(time.asctime().split()[2])
dia0=int(time.asctime().split()[3].split(":")[1])
dia=0

while True:
    if dia0>dia:
        t=time.asctime()
        #dia=int(t.split([2]))
        dia=int(t.split()[3].split(":")[1])
        T=ads.value()
        V=ads.voltage()
        f.write(t+str(T)+str(V)+"\n")
        time.sleep(5)
    else:
        break

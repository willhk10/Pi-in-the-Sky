import board
import adafruit_mpl3115a2
from datetime import datetime, timedelta


i2c = board.I2C()
sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)
sensor.sealevel_pressure = 102250

startTime = datetime.now()
curTime = startTime
nextPrintTime= curTime + timedelta(microseconds = .5)

while curTime - startTime < timedelta(seconds = 5):
    curTime =  datetime.now()
    if curTime - nextPrintTime > timedelta(microseconds = 0):
        print(f"Altitude: {sensor.altitude} \n Time: {curTime} \n")
        nextPrintTime = curTime + timedelta(microseconds = .5)

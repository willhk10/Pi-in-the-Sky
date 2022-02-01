import board
import adafruit_mpl3115a2
from datetime import datetime, timedelta, timezone
import csv
import os

i2c = board.I2C()
sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)
sensor.sealevel_pressure = 102250

est = timezone(timedelta(hours = -5)) # Creates est timezone 5:00 behind utc
startTime = datetime.now(est)
curTime = startTime
nextPrintTime= curTime + timedelta(seconds = .5)
fpath = startTime.strftime("/%m-%d-%Y~%H:%M~barometerdata.csv")
os.mkdir(fpath)
with open(fpath) as f:
    writer = csv.writer(f)
    while curTime - startTime < timedelta(seconds = 5):
        curTime =  datetime.now(est)
        if curTime - nextPrintTime > timedelta(microseconds = 0):
            print(f"Altitude: {sensor.altitude} \n Time: {curTime} \n")
            writer.writerow([curTime, sensor.altitude])
            nextPrintTime = curTime + timedelta(seconds = .5)

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
nextTime= curTime #+ timedelta(seconds = .5)
fpath = startTime.strftime("%m-%d-%Y_%H:%M_barometerdata.csv")
with open(fpath, 'w') as f:
    writer = csv.writer(f)
    while True:
        curTime = datetime.now(est)
        if curTime - nextTime > timedelta(microseconds = 0):
            #print(f"Altitude: {sensor.altitude}\nTime: {curTime}\nTimedelta: {(curTime-startTime).total_seconds()}\n")
            writer.writerow([curTime, (curTime-startTime).total_seconds(), sensor.altitude])
            nextTime = nextTime + timedelta(microseconds = 500000)

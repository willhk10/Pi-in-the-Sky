import board
import adafruit_mpl3115a2
import Adafruit_LSM303
import RPi.GPIO as GPIO
from datetime import datetime, timedelta, timezone
import csv
import os

i2c = board.I2C()
altimeter = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)
altimeter.sealevel_pressure = 102250

lsm303 = Adafruit_LSM303.LSM303()

buttonPin = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

est = timezone(timedelta(hours = -5)) # Creates est timezone 5:00 behind utc

print("Waiting for button press")
while GPIO.input(buttonPin): # Waits for a button press
    pass
while not GPIO.input(buttonPin): # Then a button release to start recording
    pass
print("Recording")

csvPath = datetime.now(est).strftime("%m-%d-%Y_%H:%M_barometerdata.csv")
with open(csvPath, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'seconds from start', 'altitude', 'pressure', 'temperature', 'accelerometer x', 'accelerometer y', 'accelerometer z']) # CSV title row
    startTime = datetime.now(est)
    nextTime = startTime + timedelta(microseconds = 500000)
    while GPIO.input(buttonPin): # Records until button pressed
        curTime = datetime.now(est)
        if True: #curTime - nextTime > timedelta(microseconds = 0):
            accel, mag = lsm303.read()
            accelX, accelY, accelZ = accel
            accelX = round(accelX/107, 3)
            accelY = round(accelY/107, 3)
            accelZ = round(accelZ/107, 3)
            secFromStart = (curTime-startTime).total_seconds()
            writer.writerow([curTime, secFromStart, altimeter.altitude, altimeter.pressure, altimeter.temperature, accelX, accelY, accelZ])
            nextTime = nextTime + timedelta(microseconds = 500000)
print("Recording Ended")

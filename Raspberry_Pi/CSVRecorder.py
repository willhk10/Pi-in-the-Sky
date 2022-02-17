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

controlButtonPin = 21
servoButtonPin = 27
servoPin = 13
rPin, gPin, bPin = 25, 23, 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(controlButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(servoButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)
GPIO.setup(servoPin, GPIO.OUT)
servo = GPIO.PWM(servoPin, 50)
openCycle = 2.5
closedCycle = 12.5
servoIsOpen = True
servo.start(openCycle)

est = timezone(timedelta(hours = -5)) # Creates est timezone 5:00 behind utc

red = (0, 1, 1)
yellow = (0, 0, 1)
green = (1, 0, 1)
blue = (1, 1, 0)
def setLED(rgb):
  GPIO.output(rPin, int(rgb[0]))
  GPIO.output(gPin, int(rgb[1]))
  GPIO.output(bPin, int(rgb[2]))

setLED(yellow)
print("Waiting for button press")
while GPIO.input(controlButtonPin): # Waits for a button press
  if not GPIO.input(servoButtonPin):
    if servoIsOpen:
      servo.ChangeDutyCycle(closedCycle)
      servoIsOpen = False
    elif not servoIsOpen:
      servo.ChangeDutyCycle(openCycle)
      servoIsOpen = True
    while not GPIO.input(servoButtonPin):
      pass # Wait for button release
while not GPIO.input(controlButtonPin): # Then a button release to start recording
  pass
print("Recording")
setLED(green)
flightData = []
startAlt = altimeter.altitude
startTime = datetime.now(est)
csvPath = startTime.strftime("%m-%d-%Y_%H:%M_barometerdata.csv")
while GPIO.input(controlButtonPin): # Records until button pressed
  curTime = datetime.now(est)
  if True:
    #accel, mag = lsm303.read()
    #accelX, accelY, accelZ = accel
    #accelX = round(accelX/107, 3)
    #accelY = round(accelY/107, 3)
    #accelZ = round(accelZ/107, 3)
    secFromStart = (curTime-startTime).total_seconds()
    #flightData.append([curTime, secFromStart, altimeter.altitude, altimeter.pressure, altimeter.temperature, accelX, accelY, accelZ])
    flightData.append([curTime, secFromStart, altimeter.altitude])

with open(csvPath, 'w') as f:
  writer = csv.writer(f)
  #writer.writerow(['timestamp', 'seconds from start', 'altitude', 'pressure', 'temperature', 'accelerometer x', 'accelerometer y', 'accelerometer z'])
  writer.writerow(['timestamp', 'seconds from start', 'altitude'])
  writer.writerows(flightData)
setLED(red)
print("Recording Ended")

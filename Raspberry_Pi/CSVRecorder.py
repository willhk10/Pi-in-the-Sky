import board
import adafruit_mpl3115a2
#import Adafruit_LSM303
import RPi.GPIO as GPIO
from datetime import datetime, timedelta, timezone
import csv
import os
from time import sleep

i2c = board.I2C()
altimeter = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)
altimeter.sealevel_pressure = 102250

#lsm303 = Adafruit_LSM303.LSM303()

recordButtonPin = 16
servoButtonPin = 12
servoPin = 13
rPin, gPin, bPin = 19, 26, 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(recordButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
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

while True:
  setLED(yellow)
  print("Waiting for button press")
  while GPIO.input(recordButtonPin): # Waits for a button press
    if not GPIO.input(servoButtonPin):
      if servoIsOpen:
        servo.ChangeDutyCycle(closedCycle)
        servoIsOpen = False
        sleep(.1)
      elif not servoIsOpen:
        servo.ChangeDutyCycle(openCycle)
        servoIsOpen = True
        sleep(.1)
      while not GPIO.input(servoButtonPin):
        pass # Wait for button release
  while not GPIO.input(recordButtonPin): # Then a button release to start recording
    pass
  print("Recording")
  setLED(green)
  sleep(.2)
  servoOpened = False
  flightData = []
  alt = altimeter.altitude
  maxAlt = alt
  startAlt = alt
  startTime = datetime.now(est)
  csvPath = startTime.strftime("/home/pi/Documents/Pi-in-the-Sky/Raspberry_Pi/CSVData/%m-%d-%Y_%H:%M_barometerdata.csv")
  while GPIO.input(recordButtonPin): # Records until button pressed
    curTime = datetime.now(est)
    lastAlt = alt
    alt = altimeter.altitude
    if alt > maxAlt:
      maxAlt = alt
    if alt + 2 < maxAlt and alt > startAlt + 6:
      servo.ChangeDutyCycle(openCycle)
      servoOpened = True
      setLED(blue)
    secFromStart = (curTime-startTime).total_seconds()
    flightData.append([curTime, secFromStart, alt, servoOpened])

  with open(csvPath, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'seconds from start', 'altitude', 'servo position'])
    writer.writerows(flightData)
  setLED(red)
  print("Recording Ended")
  sleep(.3)

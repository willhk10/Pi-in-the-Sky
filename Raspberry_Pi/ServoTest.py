import RPi.GPIO as GPIO
import time

servoPin = 13
buttonPin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
p = GPIO.PWM(servoPin, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

servoOpen = True
servoPosCycle = {True:2.5, False:12.5}

try:
  while True:
    if not GPIO.input(buttonPin):
      print("boo")
      servoOpen = not servoOpen
      p.ChangeDutyCycle(servoPosCycle[servoOpen])
      while not GPIO.input(buttonPin):
        pass

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

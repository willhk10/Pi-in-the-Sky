import RPi.GPIO as GPIO
GPIO.setwarnings(False)

rPin, bPin, gPin = 25, 23, 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

GPIO.output(rPin, True)
GPIO.output(bPin, False)
GPIO.output(gPin, False)

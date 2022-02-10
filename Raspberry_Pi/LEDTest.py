import RPi.GPIO as GPIO
GPIO.setwarnings(False)

rPin, gPin, bPin = 25, 23, 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

GPIO.output(rPin, True)
GPIO.output(bPin, False)
GPIO.output(gPin, True)

while True:
    rgb = input()
    GPIO.output(rPin, int(rgb[0]))
    GPIO.output(gPin, int(rgb[1]))
    GPIO.output(bPin, int(rgb[2]))

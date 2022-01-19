import time
import board
import adafruit_mpl3115a2

i2c = board.I2C()

sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)

sensor.sealevel_pressure = 102250

while True:
    pressure = sensor.pressure
    print(f"Pressure: {pressure}")
    altitude = sensor.altitude
    print(f"Altitude: {altitude}")
    temperature = sensor.temperature
    print(f"Temperature: {temperature}")
    time.sleep(.5)

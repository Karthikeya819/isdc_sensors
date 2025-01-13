# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries
# SPDX-License-Identifier: MIT
from time import sleep
import board
import adafruit_ms8607

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_ms8607.MS8607(i2c)

def main():
    while True:
        print("Pressure: %.2f hPa" % sensor.pressure)
        print("Temperature: %.2f C" % sensor.temperature)
        print("Humidity: %.2f %% rH" % sensor.relative_humidity)
        print("\n------------------------------------------------\n")
        sleep(1)

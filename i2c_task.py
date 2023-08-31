# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries

# SPDX-License-Identifier: Unlicense
import time
import board
import adafruit_bh1750

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_bh1750.BH1750(i2c)

while True:
    data = sensor.lux
    if data < 20:
        print("Too dark")
    elif data < 50:
        print("Dark")
    elif data < 100:
        print("Medium")
    elif data < 150:
        print("Bright")
    else:
        print("Too bright")

    time.sleep(1)


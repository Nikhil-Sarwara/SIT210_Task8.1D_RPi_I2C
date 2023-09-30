import time
import board
import adafruit_bh1750

# Create an I2C object using the default pins
i2c = board.I2C() 

# Create a BH1750 sensor object using the I2C object
sensor = adafruit_bh1750.BH1750(i2c)

# Continuously read the light intensity and print it to the console
while True:
    # Read the light intensity in lux
    data = sensor.lux

    # Print a message to the console depending on the light intensity
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

    # Wait for 1 second before reading the light intensity again
    time.sleep(1)
    

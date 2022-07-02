from roboboard import RoboBoard
from time import sleep_ms

rb = RoboBoard()

# rb.acroiris(0-255) creates a color wheel
# from 0 (GREEN) to 255 (GREEN)
while True:
    for i in range(256):
        rb.arcoiris(i)
        print(i)
        sleep_ms(5)

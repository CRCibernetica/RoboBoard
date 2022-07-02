from roboboard import RoboBoard
from time import sleep_ms

rb = RoboBoard()

# colors are RGB (Red, Green, Blue)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
PURPLE = (255,0,255)
YELLOW = (255,255,0)

rb.pixel(BLUE)
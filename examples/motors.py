from roboboard import RoboBoard
from time import sleep_ms

rb = RoboBoard()

# motor speed is from -1023 (reverse) to 1023 (forward)
# 0 is stopped
rb.motor_1(1023)
rb.motor_2(-1023)
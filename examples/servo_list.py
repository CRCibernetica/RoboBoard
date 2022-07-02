from roboboard import RoboBoard
from time import sleep_ms

rb = RoboBoard()

servo_pins = [4,5,18,19,23,25,26]
servos = []

for i, pin in enumerate(servo_pins):
    servos.append(rb.Servo(pin))

# sweep all servos
for i in range(180):
    for servo in servos:
        print(i)
        servo.angle(i)
    sleep_ms(10)
        
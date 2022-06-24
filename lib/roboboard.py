from machine import Pin, PWM
from neopixel import NeoPixel

class RoboBoard:
    def __init__(self):
        self.pixel_pin = Pin(2, Pin.OUT)
        self.np = NeoPixel(self.pixel_pin, 1)
        self.np[0] = (0,0,0)
        self.m1a = PWM(Pin(12))
        self.m1b = PWM(Pin(14))
        self.m2a = PWM(Pin(13))
        self.m2b = PWM(Pin(15))
    
    def pixel(self, color=(0,0,0)):
        self.np[0] = color
        self.np.write()
    
    def arcoiris(self, n=0):
        color = self.wheel(n)
        self.pixel(color)
    
    def motor_1(self, vel=0):
        if vel < -1023 | vel > 1023:
            print(f"velocidad no valida: {vel}")
        if vel > 0:
            self.m1a.duty(vel)
            self.m1b.duty(0)
        if vel < 0:
            self.m1a.duty(0)
            self.m1b.duty(vel * -1)
    
    def motor_2(self, vel=0):
        if vel < -1023 | vel > 1023:
            print(f"velocidad no valida: {vel}")
        if vel > 0:
            self.m2a.duty(vel)
            self.m2b.duty(0)
        if vel < 0:
            self.m2a.duty(0)
            self.m2b.duty(vel * -1)
    
    def wheel(self, pos):
        # Adafruit color wheel code
        # Input a value 0 to 255 return RGB tuple.
        if pos < 0:
            return (0, 0, 0)
        if pos > 255:
            return (0, 0, 0)
        if pos < 85:
            return (int(pos * 3), int(255 - (pos * 3)), 0)
        elif pos < 170:
            pos -= 85
            return (int(255 - pos * 3), 0, int(pos * 3))
        else:
            pos -= 170
            return (0, int(pos * 3), int(255 - pos * 3))
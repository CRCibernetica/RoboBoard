# CRCibernetica RoboBoard
The RoboBoard is an educational robotics development board created by CRCibernetica.com in Costa Rica.

The RoboBoard is based on the ESP32 microcontroller and features the following characteristics:
* ESP32-WROOM-32E microcontroller
  * 32bits @ 160MHz
  * 3.3V logic
  * 520KB SRAM
  * 16MB FLASH
  * WIFI 802.11b/g/n
  * Bluetooth V4.2 BR/EDR y Bluetooth LE
* Dual H-Bridges for motor control (800mA for each motor)
* Multi-color programmable RGB LED (WS2812B)
* Programmable using Micropython or the Arduino IDE (C/C++)
* USB-C interfaz for programming and debugging (CH340G serial converter)
* Standard .1" headers for convenient interfacing with GND and Vcc for each pin
* STEMMA/QWIIC 4-pin interface for easy connections to Adafruit and Sparkfun i2c modules
* Direct DC power for battery or power supply (5VDC - 9VDC)
* 7 pins for servos or other applications that require direct power
* 14 General Purpose I/O pins in total (7 direct power -- 7 with 3.3v logic)

## Installation
We recommend the use of the free and open source [Thonny](https://thonny.org) Integrated Development Environment (IDE). Thonny is available for Windows, Mac and Linux and comes prepackaged with all the tools to install firmware and program the CRCibernetica RoboBoard. 

### CRCibernetica RoboBoard Micropython firmware
The latest RoboBoard firmware can be downloaded here:
 * [RoboBoard firmware](https://github.com/CRCibernetica/RoboBoard/tree/main/firmware)
 
 Select the `roboboard-xxxx.bin` file and click the DOWNLOAD button on the right.
 
 ![download](/img/download.png)
 
Apart from the standard micropython modules the RoboBoard firmware includes the following:
* roboboard - modules for controlling the onboard motor drivers, the RGB LED and servos
* ssd1306 - oled display
* hcsr04 - ultrasonic sensor
* sx127x - lora radio driver
* chispa - mqtt framework for IoT and Industry 4.0 applications

The micropython firmware was built using the code and instructions found at:

[Github Micropython Repository](https://github.com/micropython/micropython)
### Getting Started
* Connect the RoboBoard to a USB port
* Open Thonny and select `Run-->Select Interpreter`
* In the `Interpreter` tab select `Micropython (ESP32)`
* Select the serial port where the RoboBoard is connected
* Click on `Install or update firmware`
* Select the serial port where the RoboBoard is connected and the location of the downloaded firmware (roboboard-xxxx.bin file)
* Click on `Install`. The process of erasing and installing the firmware will taken several minutes

[![install video](/img/installationvideo.png)](https://youtu.be/QUobo48bmSs)

## RoboBoard module 
The RoboBoard module contains helper classes for functions that are unique to the board:
* functions to control the speed and direction of `motor_1` and `motor_2`
* functions to control the onboard `RGB LED`
* functions to control standard hobby `servo motors`

[Example code can be found here](https://github.com/CRCibernetica/RoboBoard/tree/main/examples)

### General Usage
Import the RoboBoard class and create an instance
```
from roboboard import RoboBoard
rb = RoboBoard()
```
### Motor control
The two motors are named `motor_1` and `motor_2`. They can be controlled by giving them a number between -1023 (full reverse), 0 (stopped), and 1023 (full forward).
```
from roboboard import RoboBoard
rb = RoboBoard()

rb.motor_1(1023) # full forward
rb.motor_2(-1023) # full reverse
```
### RGB LED control
The onboard RGB LED can be used to indicate different modes or display how your robot is thinking. There are two functions to control the RGB LED:
* `pixel(RGB color tuple)`
* `arcoiris(number from 0 to 255)`
#### pixel()
The `pixel()` function takes in a RGB tuple and displays the color on the LED
```
from roboboard import RoboBoard
rb = RoboBoard()

# the colors are in RGB (red, green, blue format) with values between 0 and 255
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (255,0,255)

rb.pixel(BLUE)
```
#### arcoiris()
The `arcoiris()` function displays a color of the rainbow. By changing the number over time a rainbow effect can be created. The numbers are from 0 to 255.
```
from roboboard import RoboBoard
from time import sleep_ms

rb = RoboBoard()

while True:
    for i in range(256):
        rb.arcoiris(i)
        print(i)
        sleep_ms(5)
```
### Servo control
Up to 7 hobby servo motors can be controlled simultaneously using the RoboBoard.
#### Create servo instance
Multiple servo instances can be created using the `Servo(pin)` function
```
from roboboard import RoboBoard
from time import sleep_ms

rb = RoboBoard()

# Create servo1 on Pin 4, servo2 on Pin 5
servo1 = rb.Servo(4)
servo2 = rb.Servo(5)
```
#### angle(0-180)
Change the servo positions using `angle(degrees)`. By default the range is 0 - 180.
```
servo.angle(90) # change the servo position to 90 degrees
```




 


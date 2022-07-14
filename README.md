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
 
### Getting Started
Connect the 
 


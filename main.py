from roboboard import RoboBoard
from time import sleep_ms

# crear el objeto
rb = RoboBoard()

ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

# pixel utiliza tuples de RGB
rb.pixel(AZUL)
sleep_ms(1000)
rb.pixel(ROJO)
sleep_ms(1000)
rb.pixel((0,255,0))
sleep_ms(1000)

# arcoiris es una rueda de colores de 0-255 (empieza en verde termina en verde)
rb.arcoiris(125)
sleep_ms(1000)

for i in range(255):
    rb.arcoiris(i)
    sleep_ms(10)

# los motores reciben velocidades de -1023 a 1023 (detras - adelante)
rb.motor_1(1023)
rb.motor_2(-1023)
sleep_ms(2000)
rb.motor_1(0)
rb.motor_2(0)
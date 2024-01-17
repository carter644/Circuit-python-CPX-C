import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

#led13 = D13


while True:
    led.value = True
    time.sleep(0.8)
    led.value = False
    time.sleep(0.8)

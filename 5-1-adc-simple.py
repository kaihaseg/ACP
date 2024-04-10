import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc(comp, dac):
    for val in range(256):
        GPIO.output(dac, decimal2binary(val))
        sleep(0.02)
        cv = GPIO.input(comp)
        if cv == 1:
            return val

    return 256

try:
    GPIO.output(troyka, 1)
    while True:
        out = adc(comp, dac)
        voltage = out / 256 * 3.3
        print(voltage)

finally:
    GPIO.output(troyka, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()
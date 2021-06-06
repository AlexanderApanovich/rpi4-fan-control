import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

fan_pin = 18
max_temperature_celsius = 40
poll_period_sec = 5
measure_cpu_temperature_command = 'vcgencmd measure_temp'


def getCPUtemperature():
    command_result = os.popen(measure_cpu_temperature_command).readline()
    temperature = command_result.replace("temp=", "").replace("'C\n", "")
    # print("temperature is {0}".format(temperature))
    return temperature


def setFanPin(mode):
    GPIO.output(fan_pin, mode)


def turnFanOn():
    setPin(True)


def turnFanOff():
    setPin(False)


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fan_pin, GPIO.OUT)
    GPIO.setwarnings(False)


def update():
    cpuTemperature = float(getCPUtemperature())
    if cpuTemperature > max_temperature_celsius:
        turnFanOn()
    else:
        turnFanOff()


try:
    init()
    while True:
        update()
    sleep(poll_period_sec)
except KeyboardInterrupt:
    GPIO.cleanup()

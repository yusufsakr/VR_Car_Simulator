##################################################
# Code Created by "Lankash"
#  @7/4/2022
# File Contents: PID Application
#


import modules.pid as PID
import modules.sens_read as sens_read
import modules.map
import RPi.GPIO as GPIO
from time import sleep
import matplotlib as matplot
import numpy


#
# Define pins
#
piston1_open = 0
piston1_close = 6


#
# Configure Raspberry Pi Pins
#
GPIO.setWarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(piston1_open, GPIO.OUT)
GPIO.setup(piston1_close, GPIO.OUT)


#
# Initialize variables
#
sensors = [0, 0, 0, 0, 0, 0]

#
# Configure SPI connection for sensor readings
#
sens_read.SPI_MCP3008_Init()

#
# Initialize the Piston PID Parameters
#
piston_1 = PID.pid

piston_1.kp = 0.0
piston_1.kd = 0.0
piston_1.ki = 0.0


#
# Inizialize thw PWM variables
#
freq = 100
pwm_1 = GPIO.PWM(piston1_open, freq)
pwm_7 = GPIO.PWM(piston1_close, freq)


#
# Invers kinematics equations
#
setPoint_1 = 0.0

while (True):
    #
    # Receive the Sesnsor Readings via SPI
    #
    sensors = sens_read.ADC_MCP3008_Readings()

    #
    # Compute PID parameters
    #
    piston1_pwm = PID.update(piston_1, setPoint_1, sensors[0])

    #
    # PWM Output
    #
    if (setPoint_1 - sensors[0]) > 0:
        pwm_1.start(piston1_pwm)
    elif (setPoint_1 - sensors[0]) < 0:
        pwm_7.start(piston1_pwm)

##################################################
# Code Created by "Lankash"
#  @5/2/2022
# File Contents: PID Application
#


import modules.pid as PID
import modules.sens_read as sens_read
import modules.map
import RPi.GPIO as GPIO
from time import sleep
#import matplot
import numpy


#
# Define pins
#
piston1_open = 0
piston2_open = 1
piston3_open = 2
piston4_open = 3
piston5_open = 4
piston6_open = 5

piston1_close = 6
piston2_close = 7
piston3_close = 8
piston4_close = 9
piston5_close = 10
piston6_close = 11


#
# Configure Raspberry Pi Pins
#
GPIO.setWarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(piston1_open, GPIO.OUT)
GPIO.setup(piston2_open, GPIO.OUT)
GPIO.setup(piston3_open, GPIO.OUT)
GPIO.setup(piston4_open, GPIO.OUT)
GPIO.setup(piston5_open, GPIO.OUT)
GPIO.setup(piston6_open, GPIO.OUT)

GPIO.setup(piston1_close, GPIO.OUT)
GPIO.setup(piston2_close, GPIO.OUT)
GPIO.setup(piston3_close, GPIO.OUT)
GPIO.setup(piston4_close, GPIO.OUT)
GPIO.setup(piston5_close, GPIO.OUT)
GPIO.setup(piston6_close, GPIO.OUT)


#
# Initialize variables
#
sensors = [0, 0, 0, 0, 0, 0]

#
# Configure SPI connection for sensor readings
#
sens_read.SPI_MCP3008_Init()

#
# Initialize the 6 Pistons PID Parameters
#
piston_1 = PID.pid
piston_2 = PID.pid
piston_3 = PID.pid
piston_4 = PID.pid
piston_5 = PID.pid
piston_6 = PID.pid

piston_1.kp = 0.0
piston_1.kd = 0.0
piston_1.ki = 0.0

piston_2.kp = 0.0
piston_2.kd = 0.0
piston_2.ki = 0.0

piston_3.kp = 0.0
piston_3.kd = 0.0
piston_3.ki = 0.0

piston_4.kp = 0.0
piston_4.kd = 0.0
piston_4.ki = 0.0

piston_5.kp = 0.0
piston_5.kd = 0.0
piston_5.ki = 0.0

piston_6.kp = 0.0
piston_6.kd = 0.0
piston_6.ki = 0.0

#
# Inizialize thw PWM variables
#
freq = 100
pwm_1 = GPIO.PWM(piston1_open, freq)
pwm_2 = GPIO.PWM(piston2_open, freq)
pwm_3 = GPIO.PWM(piston3_open, freq)
pwm_4 = GPIO.PWM(piston4_open, freq)
pwm_5 = GPIO.PWM(piston5_open, freq)
pwm_6 = GPIO.PWM(piston6_open, freq)
pwm_7 = GPIO.PWM(piston1_close, freq)
pwm_8 = GPIO.PWM(piston2_close, freq)
pwm_9 = GPIO.PWM(piston3_close, freq)
pwm_10 = GPIO.PWM(piston4_close, freq)
pwm_11 = GPIO.PWM(piston5_close, freq)
pwm_12 = GPIO.PWM(piston6_close, freq)

#
# Invers kinematics equations
#
setPoint_1 = 0.0
setPoint_2 = 0.0
setPoint_3 = 0.0
setPoint_4 = 0.0
setPoint_5 = 0.0
setPoint_6 = 0.0


while (True):
    #
    # Receive the Sesnsor Readings via SPI
    #
    sensors = sens_read.ADC_MCP3008_Readings()

    #
    # Compute PID parameters
    #
    piston1_pwm = PID.update(piston_1, setPoint_1, sensors[0])
    piston2_pwm = PID.update(piston_2, setPoint_2, sensors[1])
    piston3_pwm = PID.update(piston_3, setPoint_3, sensors[2])
    piston4_pwm = PID.update(piston_4, setPoint_4, sensors[3])
    piston5_pwm = PID.update(piston_5, setPoint_5, sensors[4])
    piston6_pwm = PID.update(piston_6, setPoint_6, sensors[5])

    #
    # PWM Output
    #
    if (setPoint_1 - sensors[0]) > 0:
        pwm_1.start(piston1_pwm)
    elif (setPoint_1 - sensors[0]) < 0:
        pwm_7.start(piston1_pwm)

    if (setPoint_2 - sensors[1]) > 0:
        pwm_2.start(piston2_pwm)
    elif (setPoint_2 - sensors[1]) < 0:
        pwm_8.start(piston2_pwm)

    if (setPoint_3 - sensors[2]) > 0:
        pwm_3.start(piston3_pwm)
    elif (setPoint_3 - sensors[2]) < 0:
        pwm_9.start(piston3_pwm)

    if (setPoint_4 - sensors[3]) > 0:
        pwm_4.start(piston4_pwm)
    elif (setPoint_4 - sensors[3]) < 0:
        pwm_10.start(piston4_pwm)

    if (setPoint_5 - sensors[4]) > 0:
        pwm_5.start(piston5_pwm)
    elif (setPoint_5 - sensors[4]) < 0:
        pwm_11.start(piston5_pwm)

    if (setPoint_6 - sensors[5]) > 0:
        pwm_6.start(piston6_pwm)
    elif (setPoint_6 - sensors[5]) < 0:
        pwm_12.start(piston6_pwm)

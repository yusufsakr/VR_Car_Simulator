##################################################
# Code Created by "Lankash"
#  @5/2/2022
# File Contents: PWM + Piston
#

from modules.map import MAP
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

piston_ext = 5  # GPIO 5
enable_ext = 7  # GPIO 7
piston_ret = 6  # GPIO 6
enable_ret = 8  # GPIO 8

freq_ext = 100      # Frequency of the O/P signal
cycle_ext = 100      # Percentage from the fr3equency output

freq_ret = 100     # Frequency of the O/P signal
cycle_ret = 100     # Percentage from the fr3equency output

map_extr_cycle = MAP(cycle_ext, 0, 100, 22, 65)
map_ret_cycle = MAP(cycle_ret, 0, 100, 22, 65)

GPIO.setup(piston_ext, GPIO.OUT)
GPIO.setup(enable_ext, GPIO.OUT)
GPIO.setup(piston_ret, GPIO.OUT)
GPIO.setup(enable_ret, GPIO.OUT)

pwm_ext = GPIO.PWM(piston_ext, freq_ext)
pwm_ret = GPIO.PWM(piston_ret, freq_ret)

pwm_ext.start(map_extr_cycle)
pwm_ret.start(map_ret_cycle)

# while (True):
#     #GPIO.output(enable_ext, GPIO.HIGH)
#     pwm_ext.start(cycle_ext)    # Piston Extraction
#     GPIO.output(enable_ext, GPIO.LOW)
#     sleep(2)
#     pwm_ext.start(0)

#     #GPIO.output(enable_ret, GPIO.HIGH)
#     pwm_ret.start(cycle_ret)    # Piston Retraction
#     GPIO.output(enable_ret, GPIO.LOW)
#     sleep(2)
#     pwm_ret.start(0)

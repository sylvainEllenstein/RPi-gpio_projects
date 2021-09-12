from bluedot import *
from signal import pause
import sys

# import other scripts : sys.path.append('path')

# script that creates and manages interactions with BlueDot buttons
# --> main script


# remote format : acc. + brake at left, and left/right at right
bd = BlueDot(cols=6, rows=3) # MockBlueDot for tests without bluetooth client


acc = bd[0, 0]
brake = bd[0, 2]
left = bd[3, 1]
right = bd[5,1]

bd[0, 1].visible = False
bd[1, 0].visible = False
bd[1, 1].visible = False
bd[1, 2].visible = False
bd[2, 0].visible = False
bd[2, 1].visible = False
bd[2, 2].visible = False
bd[3, 0].visible = False
bd[3, 2].visible = False
bd[4, 0].visible = False
bd[4, 1].visible = False
bd[4, 2].visible = False
bd[5, 0].visible = False
bd[5, 2].visible = False


acc.square = brake.square = True
left.border = right.border = True
acc.color = brake.color = (150, 150, 150)
left.color = right.color = (200, 0, 0)

def disconnection2():
    print("Client disconnected, do you want to stop running the program ? (yes/no)")
    if input().lower() in ["yes", "\n", " "]:
        exit()
    else : 
        bd.wait_for_connection()

bd.wait_for_connection()
bd.set_when_client_disconnects = disconnection2 

# ************** Adding main.py **************** #

# -*- coding: utf-8 -*-
"""
Script for managing servos and motors for bd remoted car
"""
# This is probably the main script 

import gpiozero
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

# sys.path.append("./gpio-scripts")
# from bd_remote_car import *


# factory = PiGPIOFactory()
LeftMotorPin = "BOARD7"
RightMotorPin = "BOARD11"
rotateServoPin = None ################

# rotateServo = gpiozero.AngularServo(rotateServoPin)
leftMotor = gpiozero.Servo(LeftMotorPin)
rightMotor = gpiozero.Servo(RightMotorPin)

"""
> frame_width
    The time between control pulses, measured in seconds.
> is_active
    Composite devices are considered “active” if any of their constituent devices have a “truthy” value.
> max_pulse_width
    The control pulse width corresponding to the servo’s maximum position, measured in seconds.
> min_pulse_width
    The control pulse width corresponding to the servo’s minimum position, measured in seconds.
> pulse_width
    Returns the current pulse width controlling the servo.
"""


def goForward():
    leftMotor.min()
    rightMotor.max()

def goBackward():
    leftMotor.max()
    rightMotor.min()

def stop(): 
    leftMotor.detach()
    rightMotor.detach()

acc.when_pressed = goForward
brake.when_pressed = goBackward
acc.when_released = brake.when_released = stop




pause()

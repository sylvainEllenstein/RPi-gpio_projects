import RPi.GPIO as GPIO
import time

# to install the gpio for bash : sudo apt-get install wiringpi

# FS90R : from 0.0 to 100.0, 0 = max speed ; 
#
#  __________
#  |		|
#  |		|
#  |		|
#__|		|___________________________
#
#


def angle_to_percent(angle):
	# refaire avec nouveau moteur + enlver le jitter
	ratio = (end - start) / 180
	angleAsPercent = angle * ratio
	return start + angleAsPercent

GPIO.setmode(GPIO.BOARD) # mode de numérotation BOARD
GPIO.setup(12, GPIO.OUT)
motor1 = GPIO.PWM(12, 50) # essai avec 50 Hz

motor1.start(1) # 1 is max speed for FS90R
print("Max speed in CCW")
time.sleep(2)

dt = 7

motor1.ChangeDutyCycle(dt) # 99 is min speed ?
print(f"Trying {dt} as DutyCycle")
time.sleep(2)
motor1.stop()
print("Done !")

def tryMotor(gpioPin, freq, ratio, delt):
    motor = GPIO.PWM(gpioPin, freq)
    print(f"Trying frequence {freq} with ratio {ratio} ...")
    motor.start(ratio)
    time.sleep(delt)
    motor.stop()
    print("Done !")
    







GPIO.cleanup()

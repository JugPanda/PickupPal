from gpiozero import Robot
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10))

robot.forward()
# while True:
#     servo.angle = 90
#     sleep(2)
#     servo.angle = 0
#     sleep(2)
#     servo.angle = -90
#     sleep(2)

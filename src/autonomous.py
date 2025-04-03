from gpiozero import Robot, DistanceSensor
#from picamera2 import Picamera2, Preview
#from signal import pause
from time import sleep


#picam = Picamera2()
robot = Robot(left=(6, 5), right=(16, 18))
#sensor = DistanceSensor(echo=23, trigger=24)
#distance = sensor.value * 100
time = 0

#picam.start_preview(Preview.QTGL)
#picam.start()
class PickupPal():
	def __init__(self):
		self.left_motor = Motor(forward=6, backward=5)
		self.left_pwm = PWMOutputDevice(18)
		self.left_pwm.value = 0

	def forward(self):
		self.left_motor.forward()
		self.left_pwm.value = 0.5

	def backward(self):
		self.

while time < 5:
#	distance = sensor.value * 100

#	print(distance)
#	if distance < 30:
#		robot.stop()
#	else:
	print("drive")
	robot.backward()
	sleep(1)
	time += 1

#picam.close()

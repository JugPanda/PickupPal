from gpiozero import Robot, DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=23, trigger=24)

def read_distance():
	distance = sensor.distance * 100
	print("Distance: ", round(distance, 2), " cm")
	
while True:
	read_distance()
	sleep(0.1)

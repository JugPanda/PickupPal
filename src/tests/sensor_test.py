from gpiozero import Robot, DistanceSensor

sensor = DistanceSensor(echo=23, trigger=24)

def read_distance():
	distance = sensor.value * 100
	print("Distance: " + "{:1.2f}".format(distance) + " cm")
	
while True:
	read_distance()
	sleep(0.1)

from gpiozero import Robot, Motor, DistanceSensor, PWMOutputDevice
from picamera2 import Picamera2, Preview
from time import sleep


class PickupPal:
    def __init__(self):
        # Left motor
        self.left_motor = Motor(forward=6, backward=5)
        #self.left_pwm = PWMOutputDevice(18)
        #self.left_pwm.value = 0

        # Right motor
        self.right_motor = Motor(forward=16, backward=18)
        #self.right_pwm = PWMOutputDevice(18)
        #self.right_pwm.value = 0
        
        # Raspberry Pi camera
        self.picam = Picamera2()
        self.picam.start_preview(Preview.QTGL)
        self.picam.start()
        
        # Ultrasonic distance sensor (HC-SR04)
        self.sensor = DistanceSensor(echo=23, trigger=24)
        self.distance = self.sensor.value * 100
        self.i = 0

    def forward(self):
        self.left_motor.forward()
        self.right_motor.forward()
        #self.left_pwm.value = 0.5
        #self.right_pwm.value = 0.5

    def backward(self):
        self.left_motor.backward()
        self.right_motor.backward()
        #self.left_pwm.value = 0.5
        #self.right_pwm.value = 0.5
        
    def main(self, time):
        while self.i < time:
            if gpio_pal.distance < 30:
                gpio_pal.backward()
            else:
                gpio_pal.forward()
            gpio_pal.backward()
            sleep(1)
            self.i += 1
        self.picam.close()


gpio_pal = PickupPal()
gpio_pal.main(5)

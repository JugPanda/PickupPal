from gpiozero import Motor, PWMOutputDevice
from time import sleep


class PickupPal:
    def __init__(self):
        # Left motor
        self.left_motor = Motor(forward=19, backward=26)
        # self.left_pwm = PWMOutputDevice(18)
        # self.left_pwm.value = 0

        # Right motor
        self.right_motor = Motor(forward=17, backward=27)
        # self.right_pwm = PWMOutputDevice(18)
        # self.right_pwm.value = 0
        self.i = 0

    def forward(self):
        self.left_motor.forward()
        self.right_motor.forward()
        # self.left_pwm.value = 0.5
        # self.right_pwm.value = 0.5

    def backward(self):
        self.left_motor.backward()
        self.right_motor.backward()
        # self.left_pwm.value = 0.5
        # self.right_pwm.value = 0.5

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def main(self, time):
        self.stop()
        while self.i < time:
            print("Running")
            self.forward()
            sleep(1)
            self.i += 1
        self.stop()


gpio_pal = PickupPal()
gpio_pal.main(8)

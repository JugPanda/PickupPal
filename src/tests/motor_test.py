from gpiozero import Motor, PWMOutputDevice
from time import sleep

class PickupPal:
    def __init__(self):
        # Left motor
        self.left_motor = Motor(forward=5, backward=6)
        self.pulley_left = Motor(forward=19, backward=26)

        # Right motor
        self.right_motor = Motor(forward=21, backward=20)
        self.pulley_right = Motor(forward=17, backward=27)
        self.i = 0
        
        self.left_motor.stop()
        self.right_motor.stop()

    def forward(self):
        self.left_motor.forward()
        self.right_motor.forward()

    def backward(self):
        self.left_motor.backward()
        self.right_motor.backward()
    
    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
    
    def pulley_stop(self):
        self.pulley_left.stop()
        self.pulley_right.stop()
        
    def pulley_up(self):
        self.pulley_left.backward()
        self.pulley_right.backward()
        
    def pulley_down(self):
        self.pulley_left.forward()
        self.pulley_right.forward()
        
    def main(self, time):
        while self.i < time:
            print("Running")
            self.pulley_up()
            sleep(1)
            self.i += 1
        self.stop()
        self.pulley_stop()

gpio_pal = PickupPal()
gpio_pal.main(1)

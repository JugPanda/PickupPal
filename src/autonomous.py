from gpiozero import Robot, Motor, DistanceSensor, PWMOutputDevice
from picamera2 import Picamera2, Preview
from time import sleep
import curses


class PickupPal:
    def __init__(self):
        # Left motor
        self.left_motor = Motor(forward=6, backward=5)
        self.left_pwm = PWMOutputDevice(18)
        self.left_pwm.value = 0

        # Right motor
        self.right_motor = Motor(forward=16, backward=18)
        self.right_pwm = PWMOutputDevice(18)
        self.right_pwm.value = 0
        self.sensor = DistanceSensor(echo=23, trigger=24)
        self.distance = self.sensor.value * 100

        # Raspberry Pi camera
        self.picam = Picamera2()
        self.picam.start_preview(Preview.QTGL)
        self.picam.start()

    def forward(self):
        self.left_motor.forward()
        self.right_motor.forward()
        self.left_pwm.value = 0.5
        self.right_pwm.value = 0.5

    def backward(self):
        self.left_motor.backward()
        self.right_motor.backward()
        self.left_pwm.value = 0.5
        self.right_pwm.value = 0.5

    def map_key_to_command(self, key):
        mapa = {curses.KEY_UP: self.forward, curses.KEY_DOWN: self.backward}
        return mapa[key]

    def control(self, key):
        return self.map_key_to_command(key)


gpio_pal = PickupPal()


def main(time, window):
    next_key = None
    while time < 60:
        if next_key is None:
            key = window.getch()
            print(key)
        else:
            key = next_key
            next_key = None
        if key != 1:
            # Key was pressed
            curses.halfdelay(1)
            action = gpio_pal.control(key)
            if action:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # Key was released
            gpio_pal.left_motor.stop()

        if gpio_pal.distance < 30:
            gpio_pal.backward()
        else:
            gpio_pal.forward()
        gpio_pal.backward()
        sleep(1)
        time += 1


# picam.close()
curses.wrapper(main)

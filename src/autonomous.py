from gpiozero import Robot, Motor, DistanceSensor, PWMOutputDevice
from picamera2 import Picamera2
from ultralytics import YOLO
from time import sleep
import cv2


class PickupPal:
    def __init__(self):
        # Left motor
        self.left_motor = Motor(forward=6, backward=5)
        # self.left_pwm = PWMOutputDevice(17)
        # self.left_pwm.value = 0

        # Right motor
        self.right_motor = Motor(forward=16, backward=18)
        # self.right_pwm = PWMOutputDevice(26)
        # self.right_pwm.value = 0

        # Set up the camera with Picam
        self.picam = Picamera2()
        self.picam.preview_configuration.main.size = (1280, 1280)
        self.picam.preview_configuration.main.format = "RGB888"
        self.picam.preview_configuration.align()
        self.picam.configure("preview")
        self.picam.start()

        # Load YOLO11
        self.model = YOLO("yolo11n.pt")
        self.objects_to_detect = [0, 73]

        # Ultrasonic distance sensor (HC-SR04)
        # self.sensor = DistanceSensor(echo=23, trigger=24)
        # self.distance = self.sensor.distance * 100
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

    def left(self):
        self.backward()
        sleep(2)
        self.left_motor.stop()
        self.right_motor.stop()
        self.left_motor.forward()
        sleep(3)
        self.left_motor.stop()

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def read_distance(self):
        print("distance")
        # self.distance = self.sensor.distance * 100
        # print("Distance: ", round(self.distance, 2), " cm")

    def main(self, time):
        self.stop()
        while self.i < time:
            # Capture a frame from the camera
            frame = self.picam.capture_array()

            # Run YOLO model on the captured frame and store the results
            results = self.model(frame, imgsz=640)

            # self.read_distance()

            # if self.distance < 50:
            #    self.left()
            # else:
            #    self.forward()

            detected_objects = results[0].boxes.cls.tolist()
            object_found = False

            for obj_id in self.objects_to_detect:
                if obj_id in detected_objects:
                    object_found = True
                    print(f"Detected object with ID {obj_id}!")

                    if object_found:
                        self.forward()
                    else:
                        self.stop()

            # Output the visual detection data, we will draw this on our camera preview window
            annotated_frame = results[0].plot()

            # Display the resulting frame
            cv2.imshow("Object Detection", annotated_frame)

            # Exit the program if q is pressed
            if cv2.waitKey(1) == ord("q"):
                break

            sleep(0.1)
            self.i += 0.1
        self.stop()

        # Close all windows
        cv2.destroyAllWindows()


gpio_pal = PickupPal()
gpio_pal.main(2)

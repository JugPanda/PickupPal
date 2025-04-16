from gpiozero import Robot, Motor, DistanceSensor, PWMOutputDevice
from picamera2 import Picamera2
from ultralytics import YOLO
from time import sleep
import cv2


class PickupPal:
    def __init__(self):
        # Left motor
        self.left_motor = Motor(forward=5, backward=6)
        self.pulley_left = Motor(forward=19, backward=26)
        # self.left_pwm = PWMOutputDevice(17)
        # self.left_pwm.value = 0

        # Right motor
        self.right_motor = Motor(forward=21, backward=20)
        self.pulley_right = Motor(forward=17, backward=27)
        # self.right_pwm = PWMOutputDevice(26)
        # self.right_pwm.value = 0
        # self.left_motor.stop()
        # self.right_motor.stop()

        # Set up the camera with Picam
        self.picam = Picamera2()
        self.picam.preview_configuration.main.size = (1000, 1000)
        self.picam.preview_configuration.main.format = "RGB888"
        self.picam.preview_configuration.align()
        self.picam.configure("preview")
        self.picam.start()

        # Load YOLO11
        self.model = YOLO("yolo11n.pt")
        self.objects_to_detect = [0, 2]

        # Ultrasonic distance sensor (HC-SR04)
        self.sensor = DistanceSensor(echo=23, trigger=24)
        self.distance = self.sensor.distance * 100
        self.i = 0

    def forward(self):
        self.left_motor.forward()
        self.right_motor.forward()

    def backward(self):
        self.left_motor.backward()
        self.right_motor.backward()

    def left(self):
        self.left_motor.forward()

    def right(self):
        self.right_motor.forward()

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def pulley_up(self):
        self.pulley_left.backward()
        self.pulley_right.backward()

    def pulley_down(self):
        self.pulley_left.forward()
        self.pulley_right.forward()

    def pulley_stop(self):
        self.pulley_left.stop()
        self.pulley_right.stop()

    def read_distance(self):
        self.distance = self.sensor.distance * 100
        print("Distance: ", round(self.distance, 2), " cm")

    def main(self, time):
        try:
            while self.i < time:
                # Capture a frame from the camera
                frame = self.picam.capture_array()

                # Run YOLO model on the captured frame and store the results
                results = self.model(frame, imgsz=640)

                detected_objects = results[0].boxes.cls.tolist()

                object_found = False
                for obj_id in self.objects_to_detect:
                    if obj_id in detected_objects:
                        object_found = True
                        print(f"Detected object with ID {obj_id}!")

                self.read_distance()
                if object_found and self.distance > 5:
                    self.forward()
                elif object_found and self.distance < 5:
                    print("Object on plow")
                    self.stop()
                    self.pulley_up()
                    sleep(20)
                    self.pulley_down()
                    sleep(20)
                    self.pulley_stop()
                else:
                    print("No objects found")
                    self.stop()
                    self.backward()
                    sleep(4)
                    self.left()
                    sleep(2)
                    self.right()
                    sleep(2)

                # Output the visual detection data, we will draw this on our camera preview window
                annotated_frame = results[0].plot()

                # Display the resulting frame
                cv2.imshow("Object Detection", annotated_frame)

                # Exit the program if q is pressed
                if cv2.waitKey(1) == ord("q"):
                    break

                sleep(0.1)
                self.i += 0.1

            # Close all windows
            cv2.destroyAllWindows()
            self.stop()
            self.pulley_stop()

        except KeyboardInterrupt:
            # Close all windows
            cv2.destroyAllWindows()
            self.stop()
            self.pulley_stop()


gpio_pal = PickupPal()
gpio_pal.main(30)

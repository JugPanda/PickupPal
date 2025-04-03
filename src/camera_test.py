from picamera2 import Picamera2, Preview
from time import sleep


picam = Picamera2()

picam.start_preview(Preview.QTGL)
picam.start()
sleep(10)
#picam.start_and_record_video("Desktop/new_video.mp4", duration=10, show_preview=True)
picam.close()

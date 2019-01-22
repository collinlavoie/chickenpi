from picamera import PiCamera
import time
from time import sleep
import os
from os.path import expanduser


class Reader(object):

    _base_path = expanduser("~")

    def __init__(self, base_path=None):
        if base_path:
            self._base_path = base_path

    def get_image(self):
        image_path = self.capture_image()
        return image_path

    def capture_image(self):
        image_path = os.path.join(
                self._base_path,
                'image.{}.jpg'.format(time.strftime("%Y%m%dT%Hh%Mm%Ss"))
                )
        with PiCamera() as camera:
            camera.start_preview()
            sleep(2)
            camera.capture(image_path)
            camera.stop_preview()

        return image_path

    def capture_video(self):
        pass

try:
   from picamera import PiCamera
except:
    print "Could not import picamera"
import time
from time import sleep
import os
from os.path import expanduser


class Reader(object):

    _base_path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, base_path=None):
        if base_path:
            self._base_path = base_path

    def get_image(self):
        filename = 'image.{}.jpg'.format(time.strftime("%Y%m%dT%Hh%Mm%Ss"))
        self.capture_image(filename)
        return filename

    def save_image(self, filename):
        self.capture_image(filename)

    def capture_image(self, filename):
        with PiCamera() as camera:
            camera.start_preview()
            sleep(2)
            camera.capture(os.path.join(self._base_path, filename))
            camera.stop_preview()

    def capture_video(self):
        raise NotImplementedError

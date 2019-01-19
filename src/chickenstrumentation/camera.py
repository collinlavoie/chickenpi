from picamera import PiCamera
import time
from time import sleep
import os
from os.path import expanduser



class Reader(object):

    BASE_PATH = expanduser("~")

    @classmethod
    def get_image(cls):
        image_path = cls.capture_image()
        return image_path

    @classmethod
    def capture_image(cls):
        image_path = os.path.join(
                cls.BASE_PATH,
                'image.{}.jpg'.format(time.strftime("%Y%m%dT%Hh%Mm%Ss"))
                )
        camera = PiCamera()

        camera.start_preview()
        sleep(5)
        camera.capture(image_path)
        camera.stop_preview()
        return image_path

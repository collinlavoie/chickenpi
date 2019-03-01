try:
   from picamera import PiCamera
except:
    print "Could not import picamera"
import time
from time import sleep
import os
from os.path import expanduser

import tempfile
import subprocess
import shutil

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

    def get_video(self):
        filename = 'video.{}.mp4'.format(time.strftime("%Y%m%dT%Hh%Mm%Ss"))
        self.capture_video(filename)
        return filename

    def capture_image(self, filename):
        with PiCamera() as camera:
            camera.start_preview()
            sleep(2)
            camera.capture(os.path.join(self._base_path, filename))
            camera.stop_preview()

    def capture_video(self, filename):
        output_file = os.path.join(self._base_path, filename)
        _, h264_file = tempfile.mkstemp(suffix='.h264')
        try:
            with PiCamera() as camera:
                camera.resolution = (640, 480)
                sleep(2)
                camera.start_recording(h264_file)
                camera.wait_recording(5)
                camera.stop_recording()
            subprocess.check_call(['/usr/bin/MP4Box', '-add', h264_file, output_file])
        except subprocess.CalledProcessError, e:
            print "Failed to create MP4 container.", e
        finally:
            os.remove(h264_file)

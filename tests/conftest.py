
import os
import tempfile
import shutil
import pytest
import requests
import time

import liveandletdie

from chickenstrumentation.app import app
from chickenstrumentation.camera import Reader

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

from PIL import Image, ImageDraw

def pytest_bdd_apply_tag(tag, function):
    if tag == 'todo':
        marker = pytest.mark.skip(reason="Not implemented yet")
        marker(function)
        return True
    else:
        # Fall back to pytest-bdd's default behavior
        return None


@pytest.fixture
def camera():
    app.config['CAMERA'] = tempfile.mkdtemp()
    camera = Reader(app.config['CAMERA'])

    yield camera

    shutil.rmtree(app.config['CAMERA'])

# need another version with a mock camera
@pytest.fixture
def server():
    running_app = liveandletdie.Flask("src/chickenstrumentation/app.py")
    try:
        running_app.live(kill_port=True)
    except Exception as e:
        # Skip test if not started.
        import traceback
        print e
        pytest.fail(e.message)

    yield running_app

    running_app.die()

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("-disable-gpu")
    options.add_argument("-headless")
    b = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',
        chrome_options=options,
	)
    b.implicitly_wait(10)
    yield b
    b.quit()


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def take_mock_picture(filename=None):
    # This method should not have to know where the capture folder is.
    # The problem is that this function cannot have insight into
    # the mock camera object, which holds this information.
    # The design should be revisited
    capture_folder = "src/chickenstrumentation/capture/"
    now = time
    if not filename:
        filename = 'mock_image{}.jpg'.format(now.strftime("%Y%m%dT%Hh%Mm%Ss"))
    image_path = os.path.join(capture_folder, filename)
    img = Image.new('RGB', (512, 216), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10,10),
           "Hello Chicken\n\n{}".format(now.strftime("%F %T")),
           fill=(255,255,0))
    img.save(image_path)
    return image_path

@pytest.fixture
def mock_camera(mocker):
    mocker.patch("chickenstrumentation.camera.Reader.capture_image", side_effect=take_mock_picture)
    capture_folder = tempfile.mkdtemp()
    mock_camera = Reader(capture_folder)

    yield mock_camera

    shutil.rmtree(capture_folder)
    del mock_camera

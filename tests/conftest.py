
import os
import tempfile
import shutil
import pytest
import requests

import liveandletdie

from chickenstrumentation.app import app
from chickenstrumentation.camera import Reader

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

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

#class MyTest(LiveServerTestCase):

#    def create_app(self):
#
#        app = Flask(__name__)
#        app.config['TESTING'] = True
#        # Default port is 5000
#        app.config['LIVESERVER_PORT'] = 8943
#        # Default timeout is 5 seconds
#        app.config['LIVESERVER_TIMEOUT'] = 10
#        return app
#
#    def test_server_is_up_and_running(self):
#        response = urllib2.urlopen(self.get_server_url())
#        self.assertEqual(response.code, 200)

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

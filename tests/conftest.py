
import os
import tempfile
import shutil
import pytest

from chickenstrumentation.app import app
from chickenstrumentation.camera import Reader


@pytest.fixture
def camera():
    app.config['CAMERA'] = tempfile.mkdtemp()
    camera = Reader(app.config['CAMERA'])

    yield camera

    shutil.rmtree(app.config['CAMERA'])


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

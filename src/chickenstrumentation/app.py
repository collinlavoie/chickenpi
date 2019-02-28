from flask import Flask, render_template, send_from_directory
import os

UPLOAD_FOLDER = 'capture'
APP_HOME = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['APP_HOME'] = APP_HOME

from chickenstrumentation import probe
from chickenstrumentation import camera

@app.route('/')
def index():
    return 'index'

@app.route('/temp/')
def temp():
    data = probe.Reader.get_data()
    return render_template('temp.html', data=data)

@app.route('/web_temp/')
def web_temp():
    data = probe.WebReader.get_data()
    return render_template('temp.html', data=data)

@app.route('/view/')
def view():
    return render_template('view.html')

@app.route('/capture/<filename>')
def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/capture_image/')
def capture_image():
    capture_folder = os.path.join(app.config['APP_HOME'], app.config['UPLOAD_FOLDER'])
    camera_reader = camera.Reader(capture_folder)
    filename  = camera_reader.get_image()
    return os.path.join('/', app.config['UPLOAD_FOLDER'], filename)

@app.route('/capture_video/')
def capture_video():
    capture_folder = os.path.join(app.config['APP_HOME'], app.config['UPLOAD_FOLDER'])
    camera_reader = camera.Reader(capture_folder)
    filename  = camera_reader.get_video()
    return os.path.join('/', app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':

    # This does nothing unless you run this module with --liveandletdie flag.
    import liveandletdie
    liveandletdie.Flask.wrap(app)

    app.run()

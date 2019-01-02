from flask import Flask, render_template
app = Flask(__name__)

from chickenstrumentation import probe

@app.route('/')
def index():
    return 'index'

@app.route('/temp/')
def temp():
    data = probe.Reader.get_data()
    return render_template('temp.html', data=data)

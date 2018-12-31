from flask import Flask
app = Flask(__name__)


from flask import render_template


@app.route('/')
def index():
    return 'index'

@app.route('/temp/')
def temp():
    return render_template('temp.html')

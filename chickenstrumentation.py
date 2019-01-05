from flask import Flask, jsonify, render_template
import json
#import requests
import urllib2
#import urllib.request
#import httplib2

PROBE_LABELS = {
    'inner': '28-0000079ff834',
    'outer': '28-000007a81e55'
}

app = Flask(__name__)

@app.route("/")
def current_temp():
    data = []
    content = urllib2.urlopen("http://chickenstrument/").read()
    data = [json.loads(content)]
    return render_template('home.html', data=data)

@app.route("/24h")
def past_day():
    data = []
    content = urllib2.urlopen("http://chickenstrument/1h").read()
    # get data for desired probe
    data = [x for x in json.loads(content) if x['sensor'] in PROBE_LABELS['outer']]
    # return last 24h
    return render_template('home.html', data=data[:24])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)


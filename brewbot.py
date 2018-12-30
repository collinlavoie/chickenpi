from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/")
def hello():
    data = []
    with open('/home/collin/temp_history_15m') as file:
        for sample in [x.replace('\n', '') for x in file if "28-000007a81e55" in x]:
            ( time, sensor, temp ) = sample.split(',')
            #(time, temp)
            data.append({'sensor': sensor, 'time':time, 'temp':temp})

    return jsonify(data[-1])

@app.route("/1h")
def hourly():
    data = []
    with open('/home/collin/temp_history') as file:
        for sample in [x.replace('\n', '') for x in file]:
            ( time, sensor, temp ) = sample.split(',')
            #(time, temp)
            data.append({'sensor': sensor, 'time':time, 'temp':temp})

    return jsonify(list(reversed(data)))

@app.route("/15m")
def hi_res():
    data = []
    with open('/home/collin/temp_history_15m') as file:
        for sample in [x.replace('\n', '') for x in file]:
            ( time, sensor, temp ) = sample.split(',')
            #(time, temp)
            data.append({'sensor': sensor, 'time':time, 'temp':temp})

    return jsonify(list(reversed(data)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)



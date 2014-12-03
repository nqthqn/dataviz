from flask import Flask, render_template, jsonify, request
import csv

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def upload():

    csvfile = request.files['file']
    reader = csv.reader(csvfile)
    keys = next(reader)
    data = {}

    for k, c in zip(keys, zip(*reader)):
        data[k] = list(c)

    return jsonify(**data)

if __name__ == "__main__":
    app.run(debug=True)

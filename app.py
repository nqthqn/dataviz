from flask import Flask, render_template, jsonify
app = Flask(__name__)
app.config.from_object(__name__)
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    # TODO: Convert CSV into nice dictionary
    d = {'foo':2}
    return jsonify(**d)


if __name__ == "__main__":
    app.run(debug=True)
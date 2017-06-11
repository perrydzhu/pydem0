from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello !"


@app.route("/data")
def return_data():
    data = {
        "2011": 3,
        "2012": 18,
        "2013": 5
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

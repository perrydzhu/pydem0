#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Skipper"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)
    #app.run(host="0.0.0.0",port=8000,threaded=True)


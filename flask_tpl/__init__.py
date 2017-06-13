from flask import Flask

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(
    dict(
        FOO="hello",
        BAR="Ted!"
    )
)

from route import *

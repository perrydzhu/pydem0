from flask import render_template
from flask_tpl import app


@app.route("/debug")
def hello():
    return render_template("debug.html")



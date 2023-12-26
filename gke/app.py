from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Bem"


app.run(host='0.0.0.0', debug=True, port=5000)
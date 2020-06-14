from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/main")
@app.route("/main/<name>")
def main(name=None):
    return render_template("main.html", name=name)

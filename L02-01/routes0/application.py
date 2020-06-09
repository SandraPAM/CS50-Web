from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/sandra")
def sandra():
    return "Hello, Sandra!"

@app.route("/maria")
def maria():
    return "Hello, Maria!"
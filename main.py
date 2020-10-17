from flask import Flask

app = Flask(__name__)

@app.route('/')
def displayMain():
    return "Hello World"
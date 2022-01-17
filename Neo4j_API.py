# main.py
from flask import Flask
app = Flask(__name__)

@app.route('/basic_api/hello_world')
def hello_world():
    return 'Hello, World!'
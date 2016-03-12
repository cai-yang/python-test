# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "My Zitrone, you're beautiful!"

if __name__ == '__main__':
    app.run()

#!/usr/local/bin/python3

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index2_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


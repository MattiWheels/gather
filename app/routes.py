from flask import render_template
from app import app

@app.route('/')
def based():
    return render_template('base.html')

@app.route('/index')
def index():
    return render_template('index.html')
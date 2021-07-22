# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
# from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/smart.html')
def smart(): 
    return render_template('smart.html')

@app.route('/timeline.html')
def timeline(): 
    return render_template('timeline.html')
    
@app.route('/info.html')
def info(): 
    return render_template('info.html')

@app.route('/about.html')
def about(): 
    return render_template('about.html')

# @app.route('/profile.html')
# def profile(): 
#     return render_template('profile.html')

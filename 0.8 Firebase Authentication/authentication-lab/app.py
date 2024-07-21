from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

Config= {}



app=Flask(__name__, template_folder='templates', static_folder='static')




firebase = pyrebase.initialize_app(Config) 

auth = firebase.auth()

@app.route('/home')
def home():
    return (render_template("home.html"))



@app.route('/display')
def display():
    return (render_template("display.html"))



@app.route('/thanks')
def thanks():
    return (render_template("thanks.html"))



@app.route('/signin')
def signin():
    return (render_template("signin.html"))



@app.route('/')
def signup():
    return (render_template("signup.html"))






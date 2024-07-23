from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

Config= {'apiKey': "AIzaSyDuop6hztezl_AB7JlFGcVv1AWFHLFcos4",
  "authDomain": "iwannafinish-6f2db.firebaseapp.com",
  "projectId": "iwannafinish-6f2db",
  "storageBucket": "iwannafinish-6f2db.appspot.com",
  "messagingSenderId": "674729972281",
  "appId": "1:674729972281:web:78fe99cbee026bcad933e8",
  "databaseURL": ""
  }

app=Flask(__name__, template_folder='templates', static_folder='static')
Firebase = pyrebase.initialize_app(Config) 

auth = Firebase.auth()

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






@app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = "you are wrong!"
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('home'))
       except:
           error = "Authentication failed"
   return render_template("signup.html")






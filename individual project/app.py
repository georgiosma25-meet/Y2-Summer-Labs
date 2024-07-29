from flask import Flask, render_template, request , redirect , url_for
from flask import session as login_session
app = Flask(__name__)
import pyrebase


config = {
  "apiKey": "AIzaSyB57apRtASka-WV5Couy-P_7cwVzbybe2I",
  "authDomain": "quotef1.firebaseapp.com",
  "databaseURL": "https://quotef1-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "quotef1",
  "storageBucket": "quotef1.appspot.com",
  "messagingSenderId": "368517790138",
  "appId": "1:368517790138:web:10ac7894d50ef6542ec583",
  "databaseURL": "https://quotef1-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db =firebase.database()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('home'))
       except:
           error = "Authentication failed"
   return render_template("signup.html")





@app.route('/signin', methods=['GET', 'POST'])
def signin():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('page1'))
       except Exception as e:
           print(e)
   return render_template("signin.html")



@app.route('/quote' , methods=['GET' , 'POST'])
def quote():
    if request.method=="POST":
        quote = request.form["quote"]
        db.child("user_quotes").push({"quote":quote})
        return redirect(url_for('page1'))
    return render_template('quote.html')
 



# @app.route('/submit_quote', methods=['POST'])
# def submit_quote():
#     quote = request.form['quote']




if __name__ == '__main__':
    app.run(debug=True, port=2008)






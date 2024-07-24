from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')




@app.route('/signin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == 'example@example.com' and password == 'password':
           return redirect(url_for('home'))
        else:
            return 'Login failed. Please check your credentials.'
    return render_template('signin.html')




@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"Email: {email}, Password: {password}")
        return 'Sign up successful!'
    return render_template('signup.html')



@app.route('/quote')
def quote():
    return render_template('quote.html')













if __name__ == '__main__':
    app.run(debug=True, port=2007)

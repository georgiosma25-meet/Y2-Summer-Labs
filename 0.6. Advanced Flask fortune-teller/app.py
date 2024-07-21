from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/fortune')
def fortune():
    fortunes=[""]
    random_f=fortunes[random.randint(0,9)]
    return render_template("fortune.html",user=random_f)

if __name__ == '__main__':
    app.run(debug=True, port = 5001)

    
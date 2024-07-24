from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

# Define other routes similarly

if __name__ == '__main__':
    app.run(debug=True, port=4000)

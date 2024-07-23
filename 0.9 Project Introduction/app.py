from flask import Flask
 
app = Flask(__name__)


@app.route('/home')
def home():
    return ("<html><p>home</p></html>")


@app.route('/page1')
def page1():
    return ("<html><p>page1</p></html>")


@app.route('/signup')
def signup():
    return ("<html><p>signup</p></html>")


@app.route('/signin')
def signin():
    return ("<html><p>signin</p></html>")



@app.route('/quote')
def quote():
    return ("<html><p>quote</p></html>")









if __name__ == '__main__':
    app.run(debug = True)

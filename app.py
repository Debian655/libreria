from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/send-email')
def recordar():
    return render_template("send-email.html")
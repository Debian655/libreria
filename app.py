from flask import Flask, render_template
from auth import auth

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')

@app.route('/')
def index():
    return render_template("index.html")


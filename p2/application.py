from logging import debug
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return " Hello World\
        I am from Chitral"
app.run(debug=True)


@app.route("/about")
def about():
    return """
    <h1> PIAIC Islamabad</h1>
    i am a student of Q3
    """
app.run(debug=True)
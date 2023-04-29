from flask import flask
app= Flask(__name__)
@app.route('/')
def table():
    return 'This is an assessment.'



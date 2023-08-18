from flask import Flask

from flask import request

 

app = Flask(__name__)

 

@app.route('/')

def hello():

 

    return '<h1>hola versión 1</h1>'
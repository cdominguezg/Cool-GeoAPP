from flask import Flask

from src import return_data_well

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"
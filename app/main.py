from flask import Flask, jsonify

from src.postal_code.application.PostalCodeLister import PostalCodeLister

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify(PostalCodeLister().run().to_primitives())
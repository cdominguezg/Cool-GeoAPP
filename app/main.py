from flask import Flask

from app.controller.postal_code_controller import construct_postal_code_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(construct_postal_code_blueprint())

    return app

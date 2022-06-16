from flask import Flask

from app.controller.postal_code_controller import construct_postal_code_blueprint
from app.controller.turnover_controller import construct_turnover_blueprint
from app.dependency_injection.containers import ApplicationContainer


def create_app():
    container = ApplicationContainer()
    container.postal_code.init_resources()
    container.wire(modules=[__name__])
    app = Flask(__name__)
    app.register_blueprint(construct_postal_code_blueprint())
    app.register_blueprint(construct_turnover_blueprint())

    return app

application = create_app()
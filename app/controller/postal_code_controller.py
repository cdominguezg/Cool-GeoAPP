from flask import Blueprint, jsonify

from app.dependency_injection.containers import ApplicationContainer


def construct_postal_code_blueprint() -> Blueprint:
    postal_code_blueprint = Blueprint('postal_code', __name__, url_prefix='/postal-code')

    @postal_code_blueprint.route('', methods=['GET'])
    def list_postal_code():
        postal_code_lister = ApplicationContainer().postal_code.postal_code_list_use_case()
        result = postal_code_lister.run() or None
        result = result.to_primitives() if result is not None else None
        return jsonify(result)

    @postal_code_blueprint.route('/<id>', methods=['GET'])
    def get_postal_code(id: int):
        postal_code_finder = ApplicationContainer().postal_code.postal_code_finder_use_case()
        result = postal_code_finder.run(id) or None
        result = result.to_primitives() if result is not None else None
        return jsonify(result), 200 if result is not None else 404

    return postal_code_blueprint

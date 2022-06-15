from flask import Blueprint, jsonify, request

from app.dependency_injection.containers import ApplicationContainer
from src.turnover.domain.InvalidDateException import InvalidDateException


def construct_turnover_blueprint() -> Blueprint:
    turnover_blueprint = Blueprint('turnover', __name__, url_prefix='/turnover')

    @turnover_blueprint.route('/total', methods=['GET'])
    def list_postal_code():
        args = request.args.to_dict()
        init_date = args.get('initDate')
        end_date = args.get('endDate')

        if init_date is None or end_date is None:
            return jsonify({
                'message': 'Invalid date'
            }), 400

        turnover_total = ApplicationContainer().turnover.turnover_total_use_case()
        try:
            return jsonify(turnover_total.run(init_date, end_date))
        except InvalidDateException:
            return jsonify({
                'message': 'Invalid date'
            }), 400

    return turnover_blueprint

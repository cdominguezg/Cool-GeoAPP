from flask import Blueprint, jsonify, request

from app.dependency_injection.containers import ApplicationContainer
from src.turnover.domain.InvalidDateException import InvalidDateException


def construct_turnover_blueprint() -> Blueprint:
    turnover_blueprint = Blueprint('turnover', __name__, url_prefix='/turnover')

    @turnover_blueprint.route('/total', methods=['GET'])
    def turnover_total():
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

    @turnover_blueprint.route('/accumulated', methods=['GET'])
    def accumulated_turnover():
        args = request.args.to_dict()
        init_date = args.get('initDate')
        end_date = args.get('endDate')

        if init_date is None or end_date is None:
            return jsonify({
                'message': 'Invalid date'
            }), 400

        turnover_by_age = ApplicationContainer().turnover.turnover_by_age_use_case()
        try:
            return jsonify(turnover_by_age.run(init_date, end_date))
        except InvalidDateException:
            return jsonify({
                'message': 'Invalid date'
            }), 400

    @turnover_blueprint.route('/series', methods=['GET'])
    def series_turnover():
        args = request.args.to_dict()
        init_date = args.get('initDate')
        end_date = args.get('endDate')

        if init_date is None or end_date is None:
            return jsonify({
                'message': 'Invalid date'
            }), 400

        turnover_by_date = ApplicationContainer().turnover.turnover_by_date_use_case()
        try:
            return jsonify(turnover_by_date.run(init_date, end_date))
        except InvalidDateException:
            return jsonify({
                'message': 'Invalid date'
            }), 400

    return turnover_blueprint




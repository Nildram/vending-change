from http import HTTPStatus

from flask import Flask, abort, make_response
from flask_jsonpify import jsonify
from flask_restful import Api, Resource, reqparse
from flask_swagger_ui import get_swaggerui_blueprint

from change_calculator import (CalculationError, Calculators,
                               NegativeChangeAmountError, NegativeCoinError,
                               NegativeCountError)

app = Flask(__name__)
api = Api(app)

swagger_url = '/swagger'
swagger_blueprint = get_swaggerui_blueprint(
    swagger_url,
    '/static/swagger.yml',
    config={
        'app_name': "Change Calculator"
    }
)
app.register_blueprint(swagger_blueprint, url_prefix=swagger_url)

calculator = Calculators.non_canonical()

parser = reqparse.RequestParser()
parser.add_argument('coins', type=dict, location='json')


def get_coins():
    args = parser.parse_args()
    coins = args['coins']
    if not coins:
        abort(400, "Missing coins data")
    return {int(key): value for key, value in coins.items()}


def process_coin_data(processing_function):
    try:
        processing_function(get_coins())
    except NegativeCoinError:
        abort(400, "Coin data contains coins with negative values")
    except NegativeCountError:
        abort(400, "Coin data contains coins with negative values")


class Initialise(Resource):
    def post(self):
        process_coin_data(calculator.initialise)
        return '', HTTPStatus.NO_CONTENT


class AddCoins(Resource):
    def post(self):
        process_coin_data(calculator.add_coins)
        return '', HTTPStatus.NO_CONTENT


class GetChange(Resource):
    def get(self, amount):
        change = {}
        try:
            change = calculator.get_change(int(amount))
        except CalculationError:
            abort(404, "Requested change amount could not be calculated")
        except NegativeChangeAmountError:
            abort(400, "Requested amount is negative")
        return jsonify({'change': change})


api.add_resource(Initialise, '/change_calculator/v1.0/initialise')
api.add_resource(AddCoins, '/change_calculator/v1.0/add_coins')
api.add_resource(GetChange, '/change_calculator/v1.0/get_change/<amount>')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port='8080', debug=True)

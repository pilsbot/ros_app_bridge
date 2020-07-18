from flask import jsonify, request
from flask_restful import Resource

class Joystick(Resource):
    def post(self):
        joystick_values = request.get_json()
        print(joystick_values['x'])
        print(joystick_values['y'])
        # TODO: forward to rosnode
        return {'result': 1}, 200

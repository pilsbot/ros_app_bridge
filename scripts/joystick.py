from flask import jsonify, request
from flask_restful import Resource

class Joystick(Resource):
    def get(self, x, y):
        # TODO: forward to rosnode here
        return {'result': 1}, 200

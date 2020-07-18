#!/usr/bin/env python
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from joystick import Joystick

app = Flask(__name__)
api = Api(app)

api.add_resource(Joystick, '/joystick')

if __name__ == '__main__':
    app.run(debug=True)

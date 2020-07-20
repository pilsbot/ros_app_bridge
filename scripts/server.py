#!/usr/bin/env python
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from control import *
from common import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Joystick, '/'+restSetJoystickValues)
api.add_resource(ControlState, '/'+restGetControlState)
api.add_resource(Volume, '/'+restSetVolume)
api.add_resource(EmergencyStop, '/'+restSetEmergencyStop)
api.add_resource(Lights, '/'+restSetLightsOn)
api.add_resource(ControlMode, '/'+restSetControlMode)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)

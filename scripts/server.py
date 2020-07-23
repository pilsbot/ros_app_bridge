#!/usr/bin/env python
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from twisted.internet import reactor
from roslibpy import Ros
from control import *
from common import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Joystick, '/'+restJoystickValues)
api.add_resource(ControlState, '/'+restControlState)
api.add_resource(Volume, '/'+restVolume)
api.add_resource(EmergencyStop, '/'+restEmergencyStop)
api.add_resource(Lights, '/'+restLightOn)
api.add_resource(ControlMode, '/'+restControlMode)
api.add_resource(DrivingUser, '/'+restDrivingUser)
api.add_resource(BatteryState, '/'+restBatteryState)
api.add_resource(Velocity, '/'+restVelocity)


if __name__ == '__main__':
    #ros = Ros('localhost', 9090)
    #ros.on_ready(lambda: print('Is ROS connected?', ros.is_connected))
    #reactor.run(installSignalHandlers=False)
    app.run(host='0.0.0.0', port=5001, debug=True)

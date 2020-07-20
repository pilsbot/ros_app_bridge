from flask import jsonify, request
from flask_restful import Resource
import random


class Volume(Resource):
    def post(self):
        values = request.get_json()
        #setVolume(values['volume'])
        ret = {}
        ret['volume_sound'] = 0#getVolume()
        ret['error'] = 0
        return ret


class ControlState(Resource):
    def get(self):
        ret = {}
        ret['volume_sound'] = 0 #getVolume()
        ret['battery_percentage'] = 30 #getBatteryPercentage()
        ret['control_mode'] = 1 #getBatteryPercentage()
        ret['is_lights_on'] = False #getIsLightsOn()
        ret['is_emergency_stop'] = False #getIsEmergencyStop()
        ret['error'] = 0
        return ret


class ControlMode(Resource):
    def post(self):
        values = request.get_json()
        ret = {}
        ret['error'] = 0
        return ret


class Lights(Resource):
    def post(self):
        values = request.get_json()
        ret = {}
        ret['error'] = 0
        return ret


class EmergencyStop(Resource):
    def post(self):
        values = request.get_json()
        ret = {}
        ret['error'] = 0
        return ret


class Joystick(Resource):
    def post(self):
        values = request.get_json()
        ret = {}
        ret['error'] = 0
        return ret

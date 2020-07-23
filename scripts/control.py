from flask import jsonify, request
from flask_restful import Resource
import random
from common import *
import database as db


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
        ret[restError] = 0
        return ret

class ControlMode(Resource):
    def post(self):
        values = request.get_json()
        ret = {}
        ret['error'] = 0
        return ret

class Lights(Resource):
    def getLightOn(self):
        return int_to_bool(db.select_one(table='light'))

    def setLightOn(self, value):
        db.overwrite_one(table='light', value=bool_to_int(value))

    def post(self):
        self.setLightOn(request.get_json()[restLightOn])
        return {restError: False, restLightOn: self.getLightOn()}

    def get(self):
        return {restError: False, restLightOn: self.getLightOn()}

class DrivingUser(Resource):
    def getDrivingUser(self):
        return db.select_one(table='driver')

    def setDrivingUser(self, value):
        db.overwrite_one(table='driver', value=value)

    def post(self):
        self.setDrivingUser(request.get_json()[restDrivingUser])
        return {restError: False, restDrivingUser: self.getDrivingUser()}

    def get(self):
        return {restError: False, restDrivingUser: self.getDrivingUser()}

class BatteryState(Resource):
    def getBatteryState(self):
        return db.select_one(table='battery')

    def get(self):
        return {restError: False, restBatteryState: self.getBatteryState()}

class Velocity(Resource):
    def getVelocity(self):
        return float(db.select_one(table='velocity'))

    def get(self):
        return {restError: False, restVelocity: self.getVelocity()}

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

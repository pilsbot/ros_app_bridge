from flask import jsonify, request
from flask_restful import Resource
import random
from common import *
import database as db


class Volume(Resource):
    def getVolume(self):
        return db.select_one(table=db.table_volume)

    def setVolume(self, value):
        db.overwrite_one(table=db.table_volume, value=value)

    def post(self):
        self.setVolume(request.get_json()[restVolume])
        print(request.get_json()[restVolume])
        return {restError: False, restVolume: self.getVolume()}

    def get(self):
        return {restError: False, restVolume: self.getVolume()}


class ControlState(Resource):
    def get(self):
        return {restError: False}


class ControlMode(Resource):
    def getControlMode(self):
        return db.select_one(table=db.table_control_mode)

    def setControlMode(self, value):
        db.overwrite_one(table=db.table_control_mode, value=value)

    def post(self):
        self.setControlMode(request.get_json()[restControlMode])
        return {restError: False, restControlMode: self.getControlMode()}

    def get(self):
        return {restError: False, restControlMode: self.getControlMode()}


class Lights(Resource):
    def getLightOn(self):
        return int_to_bool(db.select_one(table=db.table_light))

    def setLightOn(self, value):
        db.overwrite_one(table=db.table_light, value=bool_to_int(value))

    def post(self):
        self.setLightOn(request.get_json()[restLightOn])
        return {restError: False, restLightOn: self.getLightOn()}

    def get(self):
        return {restError: False, restLightOn: self.getLightOn()}


class DrivingUser(Resource):
    def getDrivingUser(self):
        return db.select_one(table=db.table_driver)

    def setDrivingUser(self, value):
        db.overwrite_one(table=db.table_driver, value=value)

    def post(self):
        self.setDrivingUser(request.get_json()[restDrivingUser])
        return {restError: False, restDrivingUser: self.getDrivingUser()}

    def get(self):
        return {restError: False, restDrivingUser: self.getDrivingUser()}


class BatteryState(Resource):
    def getBatteryState(self):
        return db.select_one(table=db.table_battery)

    def get(self):
        return {restError: False, restBatteryState: self.getBatteryState()}


class Velocity(Resource):
    def getVelocity(self):
        return float(db.select_one(table=db.table_velocity))

    def get(self):
        return {restError: False, restVelocity: self.getVelocity()}


class EmergencyStop(Resource):
    def getLightOn(self):
        return int_to_bool(db.select_one(table=db.table_emergency_stop))

    def setLightOn(self, value):
        db.overwrite_one(table=db.table_emergency_stop, value=bool_to_int(value))

    def post(self):
        self.setEmergencyStop(request.get_json()[restEmergencyStop])
        return {restError: False, restEmergencyStop: self.getEmergencyStop()}

    def get(self):
        return {restError: False, restEmergencyStop: self.getEmergencyStop()}


class Joystick(Resource):
    def post(self):
        values = request.get_json()
        ret = {}
        ret['error'] = 0
        return ret

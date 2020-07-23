restControlState = 'control_state'
restVolume = 'volume'
restControlMode = 'control_mode'
restEmergencyStop = 'emergency_stop'
restJoystickValues = 'joystick_values'
restLightOn = 'light_on'
restDrivingUser = 'driving_user'
restBatteryState = 'battery'
restError = 'error'
restVelocity = 'velocity'


def bool_to_int(value):
    inp = 0
    if value:
        inp = 1
    return inp

def int_to_bool(value):
    if value == 0:
        return False
    return True

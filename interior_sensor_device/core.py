from pyjarvis.core import sensor_client
from pyjarvis.model import Measurement, SensorDevice

from . import temperature_sensor


class NoDeviceFound(Exception):
    """
    Will be thrown when no device was found.
    """
    pass


def send_humi_and_temp(request_config, device_id, source_pin):
    """Sends the humidity and temperature of the room to jARVIS"""
    humi, temp = temperature_sensor.get_humidity_and_temperature(device_id, source_pin)
    sensor_client.post_measurement(request_config, humi)
    sensor_client.post_measurement(request_config, temp)


def nested_send_movement_detected(request_config, device_id):
    """
    Uses the send_movement_detected function and encapsulated it into a lambda with a device id.

    :param request_config: Used for sending the measurement
    :param device_id: Will be put into the lambda
    :return: function for being executed by the movement detected listener
    """
    return lambda _channel: send_movement_detected(request_config, device_id)


def send_movement_detected(request_config, device_id):
    """Sends a measurement to jARVIS when a movement was detected."""
    measurement = Measurement("movement_detected", 1, device_id)
    sensor_client.post_measurement(request_config, measurement)


def get_device_id(request_config, external_device_id):
    """Requests a device from jARVIS and return its ID"""
    device_resp = sensor_client.get_sensor_device_by_external_id(request_config, external_device_id)
    if device_resp.status_code == 200:
        return SensorDevice.from_json(device_resp.json()).id
    else:
        raise NoDeviceFound("No device was found for external id " + external_device_id)

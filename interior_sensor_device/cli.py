from time import sleep
from interior_sensor_device.config import SensorConfig
from interior_sensor_device.passiv_infrared_sensor import create_movement_detector
from .core import nested_send_movement_detected, send_humi_and_temp, get_device_id


def main(sensor_config: SensorConfig):
    device_id = get_device_id(sensor_config.request_config, sensor_config.external_id)

    send_movement_detected = nested_send_movement_detected(sensor_config.request_config, device_id)
    with create_movement_detector(sensor_config.movement_detector_pin, send_movement_detected) as movement_detector:
        movement_detector.run()
        while True:
            sleep(sensor_config.delay_in_seconds)
            send_humi_and_temp(sensor_config.request_config, device_id, sensor_config.humidity_and_temp_pin)

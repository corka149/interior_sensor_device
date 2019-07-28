from time import sleep
from . import config
from interior_sensor_device.config import SensorConfig
from interior_sensor_device.passiv_infrared_sensor import create_movement_detector
from .core import nested_send_movement_detected, send_humi_and_temp, get_device_id


def main(sensor_config: SensorConfig, sleep_in_secs=5):
    device_id = get_device_id(sensor_config.request_config, sensor_config.external_id)

    send_movement_detected = nested_send_movement_detected(sensor_config.request_config, device_id)
    with create_movement_detector(sensor_config.movement_detector_pin, send_movement_detected) as movement_detector:
        movement_detector.run()
        while True:
            sleep(sleep_in_secs)
            send_humi_and_temp(sensor_config.request_config, device_id, sensor_config.humidity_and_temp_pin)


if __name__ == '__main__':
    sensor_conf = config.get_config()
    main(sensor_conf)

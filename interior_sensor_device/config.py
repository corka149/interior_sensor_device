import sys
from pyjarvis.core.config import RequestConfig


class NoExternalIdProvidedError(Exception):
    pass


class SensorConfig:

    def __init__(self, humidity_and_temp_pin, movement_detector_pin, delay_in_seconds, external_id, request_config):
        self.humidity_and_temp_pin = humidity_and_temp_pin
        self.movement_detector_pin = movement_detector_pin
        self.delay_in_seconds = delay_in_seconds
        self.external_id = external_id
        self.request_config = request_config


def get_config():
    args = sys.argv
    ht_pin = int(__find_arg__("humidity_and_temp_pin", 4, args))
    md_pin = int(__find_arg__("movement_detector_pin", 17, args))
    dis = int(__find_arg__("delay_in_seconds", "5", args))
    external_id = __find_arg__("external_id", None, args)
    if external_id is None:
        raise NoExternalIdProvidedError("External device id must be provided")

    protocol = __find_arg__("protocol", "http", args)
    host = __find_arg__("host", "localhost", args)
    port = int(__find_arg__("port", 4000, args))

    rc = RequestConfig(protocol, host, port)
    return SensorConfig(ht_pin, md_pin, dis, external_id, rc)


def __find_arg__(arg, default, args):
    findings = filter(lambda item: (arg + "=") in item, args)
    findings = list(findings)
    if len(findings) > 0:
        return findings[0].replace(arg + "=", "")
    else:
        return default

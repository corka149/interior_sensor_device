import Adafruit_DHT
from pyjarvis.model import Measurement


def get_humidity_and_temperature(device_id, sensor=Adafruit_DHT.DHT11, pin=4):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is None or temperature is None:
        return None
    humidity = Measurement("humidity", humidity, device_id)
    temperature = Measurement("temperature", temperature, device_id)
    return humidity, temperature

import Adafruit_DHT
from pyjarvis.model import Measurement


def get_humidity_and_temperature(device_id, pin=4):
    """Reads the humidity and temperature from DHT11."""
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)
    if humidity is None or temperature is None:
        return None
    humidity = Measurement("humidity", humidity, device_id)
    temperature = Measurement("temperature", temperature, device_id)
    return humidity, temperature

import RPi.GPIO as GPIO
from contextlib import contextmanager


class MovementDetector:

    def __init__(self, pin, action):
        """
        WARNING - create a MovementDetector via `create_movement_detector`

        :param pin: Pin on which the sensor is connected
        :param action: Function which will performed when a movement was detected
        """
        self.pin = pin
        self.action = action
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)

    def run(self):
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.action)


@contextmanager
def create_movement_detector(pin, action):
    """
    Creates MovementDetector with context.

    :param pin: Pin on which the sensor is connected
    :param action: Function which will performed when a movement was detected
    """
    try:
        detector = MovementDetector(pin, action)
        yield detector
    finally:
        GPIO.cleanup()

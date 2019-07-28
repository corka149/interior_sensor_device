# Interior sensor device

A simple sensor based on Raspberry Pi Zero WH and Python. It has a humidity&temperature sensor and movement detector.

## Requirements

- Python >= 3.7

## Configs via CLI

### Sensors
    NAME                    DEFAULT
    humidity_and_temp_pin   4
    movement_detector_pin   17
    delay_in_seconds        5
    external_id             No default - required!!!
    
### Jarvis
    NAME        DEFAULT
    protocol    http
    host        localhost
    port        4000
    
### Example

    python -m interior_sensor_device external_id=f8379a95-2287-41d6-a925-52fa4b0b5cc3 delay_in_seconds=20
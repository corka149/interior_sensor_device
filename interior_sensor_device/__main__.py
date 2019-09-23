from . import config
from . import cli


if __name__ == '__main__':
    sensor_conf = config.get_config()
    cli.main(sensor_conf)

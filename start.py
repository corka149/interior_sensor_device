import sys
from interior_sensor_device import cli, config

sys.argv.append("delay_in_seconds=20")
sys.argv.append("external_id=f8379a95-2287-41d6-a925-52fa4b0b5cc3")

sys.argv.append("protocol=http")
sys.argv.append("host=localhost")
sys.argv.append("port=4000")

conf = config.get_config()
cli.main(conf)

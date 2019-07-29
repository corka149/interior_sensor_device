import unittest
from interior_sensor_device import config


class MyTestCase(unittest.TestCase):

    def test__find_arg__(self):
        args = ["port=3000", "pin=4"]
        port = config.__find_arg__("port", 4000, args)
        pin = config.__find_arg__("pin", 5, args)
        self.assertEqual("3000", port)
        self.assertEqual("4", pin)


if __name__ == '__main__':
    unittest.main()

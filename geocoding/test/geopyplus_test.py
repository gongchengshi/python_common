import unittest
from python_common.geocoding.geopyplus import GeoPyPlus


class TestGeoPyPlus(unittest.TestCase):
    def basic_test(self):
        target = GeoPyPlus(config_path='../geocoding/test/example.cfg')
        actual = target.geocode('Clatskanie, Oregon, USA')
        print actual.latitude, actual.longitude

# TestGeoPyPlus().basic_test()

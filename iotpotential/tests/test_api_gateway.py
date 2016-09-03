import unittest

from iotpotential.api_gateway import ApiGateway


class MyTestCase(unittest.TestCase):
    def test_authenticate(self):
        ApiGateway()._authenticate()
        self.assertIsNotNone(ApiGateway.ACCESS_TOKEN)

    def test_get_location(self):
        result = ApiGateway().get_current_location()
        self.assertIsNotNone(result.get('latitude'))
        self.assertIsNotNone(result.get('altitude'))
        self.assertIsNotNone(result.get('longitude'))


if __name__ == '__main__':
    unittest.main()

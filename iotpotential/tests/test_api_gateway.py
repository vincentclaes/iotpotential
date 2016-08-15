import unittest
from my_examples.iotpotential.api_gateway import ApiGateway

class MyTestCase(unittest.TestCase):
    def test_authenticate(self):
        ApiGateway()._authenticate()
        self.assertEqual(True, False)

    def test_get_location(self):
        ApiGateway().get_current_location()


if __name__ == '__main__':
    unittest.main()

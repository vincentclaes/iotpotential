import unittest
from iotpotential.location import LocationHistory
import path
import os
current_dir = os.path.dirname(__file__)

class MyTestCase(unittest.TestCase):
    def test_read_json_file(self):
        self.assertEqual(LocationHistory.read_history(os.path.join(current_dir,'resources','read_json.json')), [[50.878755, 4.697177], [50.876943, 4.700536]])


if __name__ == '__main__':
    unittest.main()

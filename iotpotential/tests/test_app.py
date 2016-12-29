import unittest

import mock

import app
from iotpotential.services.location import LastSeenLocation
from iotpotential.services.location import LocationHistory


class MyTestCase(unittest.TestCase):
    #@unittest.skip('test printing of location manually')
    @mock.patch('iotpotential.location.ApiGateway.get_current_location')
    def test_print_new_locations(self, m_location):
        m_location.side_effect = [{u'latitude': 50.88333, u'altitude': 19.0, u'longitude': 4.684252},
                                  {u'latitude': 50.88450, u'altitude': 19.0, u'longitude': 4.684252},
                                  {u'latitude': 50.88550, u'altitude': 19.0, u'longitude': 4.684252},
                                  {u'latitude': 50.88650, u'altitude': 19.0, u'longitude': 4.684252}]
        app.main()



if __name__ == '__main__':
    unittest.main()

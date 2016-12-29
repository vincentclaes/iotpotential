import time
from datetime import datetime

from iotpotential import logger
from iotpotential.api_gateway import ApiGateway
from iotpotential.database import db_session
from iotpotential.models.models import DeviceLocation


class LocationService(object):
    def __init__(self):
        pass

    def run(self):
        try:
            while True:
                time.sleep(1)
                self._update_current_location()
                logger.info(DeviceLocation.query.all())
        finally:
            logger.info('remove db session before exiting ...')
            db_session.remove()

    def _update_current_location(self):
        current_location = ApiGateway.get_current_location()
        _lat, _long, _timestamp = self.parse_current_location(current_location)
        self._push_to_db(_lat, _long, _timestamp)

    def parse_current_location(self, current_location):
        gps_meter_value = current_location.get('gpsMeterValue')
        _lat = gps_meter_value.get('latitude')
        _long = gps_meter_value.get('longitude')
        _timestamp = datetime.fromtimestamp(gps_meter_value.get('timestamp'))
        return _lat, _long, _timestamp


    def _push_to_db(self, _lat, _long, _timestamp):
        if _lat != 0.0 and _long != 0.0:
            if _lat != LastSeenLocation.latitude or _long != LastSeenLocation.longitude:
                logger.info('found a new one ! update location : lat {0}, long {1}'.format(_lat, _long))
                LastSeenLocation.set_last_seen_location(_lat, _long)
                dl = DeviceLocation(_timestamp, _lat, _long)
                db_session.add(dl)
                db_session.commit()


class LastSeenLocation(object):
    latitude = None
    longitude = None

    @staticmethod
    def set_last_seen_location(latitude, longitude):
        LastSeenLocation.latitude = latitude
        LastSeenLocation.longitude = longitude


# class LocationHistory(object):
#     LOCATION_HISTORY = os.path.join(current_dir, 'location_history.json')
#     location_history = []
#     markers = []
#     polylines = []
#
#     def __init__(self):
#         pass
#         # print 'init location history'
#         #history = LocationHistory.read_history()
#         #LocationHistory.location_history.append(history)
#         # [LocationHistory.append_coordinates(_lat, _long) for _lat, _long in history]
#         # for _lat, _long in history:
#         #     LocationHistory.append_marker(_lat, _long)
#         # if history:
#         #     LastSeenLocation.latitude = LocationHistory.location_history[-1][0]
#         #     LastSeenLocation.longitude = LocationHistory.location_history[-1][1]
#
#     @staticmethod
#     def get_location():
#         try:
#             while True:
#                 all_devicelocations = DeviceLocation.query.all()
#                 logger.info('found {} devicelocations ons aws rds'.format(len(all_devicelocations)))
#                 LocationHistory.markers = [] # init list because we are going to add all points all over again
#                 LocationHistory.polylines = [] # idem
#                 for devicelocation in all_devicelocations:
#                     LocationHistory.create_polylines_list(devicelocation.lat, devicelocation.long)
#                     LocationHistory.create_markers_list(devicelocation.lat, devicelocation.long)
#                 time.sleep(3)
#         finally:
#             logger.info('remove db session before exiting ...')
#             db_session.remove()
#     @staticmethod
#     def create_polylines_list(latitude, longitude):
#         LocationHistory.polylines.append({'lat': latitude,
#                                           'lng': longitude})
#
#     @staticmethod
#     def create_markers_list(latitude, longitude):
#         LocationHistory.markers.append({
#             'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
#             'lat': latitude,
#             'lng': longitude,
#             'infobox': 'lat:{0}, lng:{1}. #{2}'.format(latitude, longitude, len(LocationHistory.markers) + 1)
#         })


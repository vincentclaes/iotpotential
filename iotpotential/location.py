import json
import logging
import os
import time

from api_gateway import ApiGateway
from static import icons

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
current_dir = os.path.dirname(__file__)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)


class Location(object):
    def __init__(self):
        self.lh = LocationHistory()

    def continuously_get_current_location(self):
        while True:
            time.sleep(0.1)
            self.get_current_location()

    def update_current_location(self, location):
        _lat = location.get('latitude')
        _long = location.get('longitude')
        if _lat != 0.0 and _long != 0.0:
            if _lat != LastSeenLocation.latitude or _long != LastSeenLocation.longitude:
                LastSeenLocation.set_last_seen_location(_lat, _long)
                LocationHistory.append_coordinates(LastSeenLocation.latitude, LastSeenLocation.longitude)
                LocationHistory.append_marker(LastSeenLocation.latitude, LastSeenLocation.longitude)
                logger.info('update location : lat {0}, long {1}'.format(_lat, _long))

    def get_current_location(self):
        logger.info('last location : {}'.format(LocationHistory.location_history))
        current_location = ApiGateway.get_current_location()
        self.update_current_location(current_location)


class LastSeenLocation(object):
    latitude = None
    longitude = None

    @staticmethod
    def set_last_seen_location(latitude, longitude):
        LastSeenLocation.latitude = latitude
        LastSeenLocation.longitude = longitude


class LocationHistory(object):
    LOCATION_HISTORY = os.path.join(current_dir, 'location_history.json')
    location_history = []

    marker_history = []

    def __init__(self):
        history = LocationHistory.read_history()
        LocationHistory.location_history = history
        for lat, long in history:
            LocationHistory.append_marker(lat,long)
        if history:
            LastSeenLocation.latitude = LocationHistory.location_history[-1][0]
            LastSeenLocation.longitude = LocationHistory.location_history[-1][1]

    @staticmethod
    def append_coordinates(latitude, longitude):
        LocationHistory.location_history.append([latitude, longitude])

    @staticmethod
    def append_marker(latitude, longitude):
        LocationHistory.marker_history.append({
            'icon': icons.dots.red,
            'lat': latitude,
            'lng': longitude,
            'infobox': 'lat:{0}, lng:{1}. #{2}'.format(latitude, longitude, len(LocationHistory.marker_history) + 1)
        })

    @staticmethod
    def read_history(file_path=LOCATION_HISTORY):
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def write_history(file_path=LOCATION_HISTORY):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        _file_path, ext = os.path.splitext(file_path)
        file_path_time_based = _file_path + '-' + timestr + ext
        with open(file_path_time_based, 'w') as f:
            json.dump(LocationHistory.location_history, f)
        with open(file_path, 'r+') as f:
            json.dump(LocationHistory.location_history, f)

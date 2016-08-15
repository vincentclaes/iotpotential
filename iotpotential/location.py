import json
import logging
import os
import time

from api_gateway import ApiGateway

logging.getLogger()
current_dir = os.path.dirname(__file__)


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
        if LastSeenLocation.latitude and LastSeenLocation.longitude is not None:
            if _lat != LastSeenLocation.latitude or _long != LastSeenLocation.longitude:
                LastSeenLocation.set_last_seen_location(_lat, _long)
                self.lh.location_history.append([LastSeenLocation.latitude, LastSeenLocation.longitude])
                logging.info('update location : lat {0}, long {1}'.format(_lat, _long))
        else:
            LastSeenLocation.set_last_seen_location(_lat, _long)
            self.lh.location_history.append([LastSeenLocation.latitude, LastSeenLocation.longitude])
            logging.info('update location : lat {0}, long {1}'.format(_lat, _long))


    def get_current_location(self):
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
    LOCATION_HISTORY = os.path.join(current_dir,'location_history.json')
    location_history = None

    def __init__(self):
        LocationHistory.location_history = LocationHistory.read_history()

    @staticmethod
    def read_history(file_path=LOCATION_HISTORY):
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def write_history(file_path=LOCATION_HISTORY):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        _file_path, ext = os.path.splitext(file_path)
        file_path_time_based = _file_path + '-'+timestr + ext
        with open(file_path_time_based, 'w') as f:
            json.dump(LocationHistory.location_history, f)
        with open(file_path, 'r+') as f:
            json.dump(LocationHistory.location_history, f)

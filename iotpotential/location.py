import json
import os
import time

from api_gateway import ApiGateway
from iotpotential import logger, current_dir
from iotpotential.database import db_session
from iotpotential.models import DeviceLocation

class Location(object):
    def __init__(self):
        print 'init location'
        self.lh = LocationHistory()

    def continuously_get_current_location(self):
        while True:
            time.sleep(1)
            # print 'getting location'
            self.get_current_location()
            logger.info('query all : ')
            logger.info(DeviceLocation.query.all())

    def get_current_location(self):
        logger.info('get last location')
        current_location = ApiGateway.get_current_location()
        self.update_current_location(current_location)

    def update_current_location(self, location):
        _lat = location.get('latitude')
        _long = location.get('longitude')
        if _lat != 0.0 and _long != 0.0:
            if _lat != LastSeenLocation.latitude or _long != LastSeenLocation.longitude:
                LastSeenLocation.set_last_seen_location(_lat, _long)
                LocationHistory.append_coordinates(LastSeenLocation.latitude, LastSeenLocation.longitude)
                LocationHistory.append_marker(LastSeenLocation.latitude, LastSeenLocation.longitude)
                LocationHistory.location_history.append([LastSeenLocation.latitude, LastSeenLocation.longitude])
                logger.info('found a new one ! update location : lat {0}, long {1}'.format(_lat, _long))

                # add to SqlLite
                dl = DeviceLocation(_lat, _long)
                db_session.add(dl)
                db_session.commit()



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
    markers = []
    polylines = []

    def __init__(self):
        # print 'init location history'
        history = LocationHistory.read_history()
        LocationHistory.location_history.append(history)
        [LocationHistory.append_coordinates(_lat, _long) for _lat, _long in history]
        for _lat, _long in history:
            LocationHistory.append_marker(_lat, _long)
        if history:
            LastSeenLocation.latitude = LocationHistory.location_history[-1][0]
            LastSeenLocation.longitude = LocationHistory.location_history[-1][1]

    @staticmethod
    def append_coordinates(latitude, longitude):
        LocationHistory.polylines.append({'lat': latitude,
                                          'lng': longitude})

    @staticmethod
    def append_marker(latitude, longitude):
        LocationHistory.markers.append({
            'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
            'lat': latitude,
            'lng': longitude,
            'infobox': 'lat:{0}, lng:{1}. #{2}'.format(latitude, longitude, len(LocationHistory.markers) + 1)
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

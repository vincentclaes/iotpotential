from sqlalchemy import Column, Integer, String, Float, DateTime
from iotpotential.database import Base

class DeviceLocation(Base):
    __tablename__ = 'DeviceLocation'
    id = Column(Integer, primary_key=True)
    device_id = Column(String(54))
    timestamp = Column(DateTime)
    lat = Column(Float(53))
    long = Column(Float(53))
    alt = Column(Float(53))


    def __init__(self, timestamp, lat, long, alt=0):
        self.device_id = '1C8779C000000156'
        self.timestamp = timestamp
        self.lat = lat
        self.long = long
        self.alt = alt

    def __repr__(self):
        return '<Device {} - {}:{} - time {}>'.format(self.id, self.lat, self.long, self.timestamp)
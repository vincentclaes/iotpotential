from sqlalchemy import Column, Integer, String, Float
from iotpotential.database import Base

class DeviceLocation(Base):
    __tablename__ = 'DeviceLocation'
    id = Column(Integer, primary_key=True)
    device_id = Column(String(64))
    lat = Column(Float(64))
    long = Column(Float(64))
    alt = Column(Float(64))


    def __init__(self, lat, long, alt=0):
        self.device_id = '1C8779C0000000C9'
        self.lat = lat
        self.long = long
        self.alt = alt

    def __repr__(self):
        return '<Device {} - {}:{}>'.format(self.id, self.lat, self.long)
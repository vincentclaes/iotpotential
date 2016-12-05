from app import db


class DeviceLocation(db.Model):
    __tablename__ = 'DeviceLocation'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(64), primary_key=True)
    lat = db.Column(db.Float(64))
    long = db.Column(db.Float(64))
    alt = db.Column(db.Float(64))

    def __init__(self, lat, long, alt=0):
        self.device_id = '1C8779C0000000C9'
        self.lat = lat
        self.long = long
        self.alt = alt


    def __repr__(self):
        return '<Device {} - {}:{}>'.format(self.id, self.lat, self.long)
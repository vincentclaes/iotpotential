from app import db


class DeviceLocation(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    lat = db.Column(db.Float(64))
    long = db.Column(db.Float(64))
    alt = db.Column(db.Float(64))


    def __repr__(self):
        return '<Device {} - {}:{}>'.format(self.id, self.lat, self.long)
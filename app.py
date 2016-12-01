# coding: utf-8

from flask import Flask, render_template
# noinspection PyPackageRequirements
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from threading import Thread

app = Flask(__name__, template_folder="templates")
app.config.from_object('config')


GoogleMaps(app, key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")
from iotpotential.location import LocationHistory
from iotpotential.location import Location

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

@app.route('/')
def fullmap():
    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:100%;"
            "width:100%;"
            "top:0;"
            "left:0;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=50.879044,
        lng=4.701482,
        markers=LocationHistory.markers,
        polylines=[{
            'stroke_color': ' #dd4b39',
            'stroke_opacity': 1.0,
            'stroke_weight': 3,
            'path': LocationHistory.polylines
        }],
    )

    return render_template('example_fullmap.html', fullmap=fullmap)

def main():
    l = Location()
    t = Thread(target=l.continuously_get_current_location).start()
    app.run(debug=True, use_reloader=True,host='0.0.0.0')

if __name__ == '__main__':
    main()
# coding: utf-8

from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from iotpotential.location import (Location, LastSeenLocation, LocationHistory)
from threading import Thread

app = Flask(__name__, template_folder="templates")

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyDigFY04sXaaKV59x_-qR4tq5oCxcZwaYs"

# you can also pass key here
GoogleMaps(app, key="AIzaSyDigFY04sXaaKV59x_-qR4tq5oCxcZwaYs")


@app.route('/')
def fullmap():
    try:
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
            lat=LastSeenLocation.latitude,
            lng=LastSeenLocation.longitude,
           polylines=[LocationHistory.location_history]
        )
        return render_template('example_fullmap.html', fullmap=fullmap)
    finally:
        LocationHistory.write_history()

if __name__ == "__main__":
    l = Location()
    t = Thread(target=l.continuously_get_current_location)
    t.start()
    app.run(debug=True, use_reloader=True)

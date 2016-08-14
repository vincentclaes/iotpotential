# coding: utf-8

from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from iotpotential.location import (Location, LastSeenLocation, LocationHistory)
from threading import Thread

app = Flask(__name__, template_folder="templates")

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4"

# you can also pass key here
GoogleMaps(app, key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")


@app.route('/fullmap')
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
            # markers=[
            #     LastSeenLocation.location_history
            # ],
            # polylines={
            #     'stroke_color': '#0066ff',
            #     'stroke_opacity': 1.0,
            #     'stroke_weight': 3,
            #     'path': LastSeenLocation.location_history
            # }

            # maptype = "TERRAIN",
            # zoom="5"
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

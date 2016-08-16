# coding: utf-8

from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from iotpotential.location import (Location, LastSeenLocation, LocationHistory)
from threading import Thread

app = Flask(__name__, template_folder="templates")

# you can set key as config
#app.config['GOOGLEMAPS_KEY'] = "AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4"

# you can also pass key here
GoogleMaps(app, key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")

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
        #lat=LastSeenLocation.latitude,
        lat=50.879044,
        #lng=LastSeenLocation.longitude,
        lng=4.701482,
        # markers=[
        #     {
        #         'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
        #         'lat': 37.4419,
        #         'lng': -122.1419,
        #         'infobox': "Hello I am <b style='color:green;'>GREEN</b>!"
        #     },
        #     {
        #         'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
        #         'lat': 37.4300,
        #         'lng': -122.1400,
        #         'infobox': "Hello I am <b style='color:blue;'>BLUE</b>!"
        #     },
        #     {
        #         'icon': icons.dots.yellow,
        #         'title': 'Click Here',
        #         'lat': 37.4500,
        #         'lng': -122.1350,
        #         'infobox': (
        #             "Hello I am <b style='color:#ffcc00;'>YELLOW</b>!"
        #             "<h2>It is HTML title</h2>"
        #             "<img src='//placehold.it/50'>"
        #             "<br>Images allowed!"
        #         )
        #     }
        # ],
        # maptype = "TERRAIN",
        # zoom="5"
    )
    return render_template('example_fullmap.html', fullmap=fullmap)


if __name__ == "__main__":
    l = Location()
    t = Thread(target=l.continuously_get_current_location)
    t.start()
    app.run(debug=True, use_reloader=True)

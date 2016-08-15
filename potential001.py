from flask import Flask, render_template, request, redirect
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from iotpotential.location import (Location, LastSeenLocation, LocationHistory)
from threading import Thread



app = Flask(__name__, template_folder="templates")

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyDigFY04sXaaKV59x_-qR4tq5oCxcZwaYs"

# Initialize the extension
GoogleMaps(app)



@app.route('/google8119fc9c07d90f07.html')
def googleverification():
    return render_template('google8119fc9c07d90f07.html')

@app.route('/fullmap')
def fullmap():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template('example_fullmap.html', mymap=mymap, sndmap=sndmap)

if __name__ == '__main__':
  
    app.run(debug=True, use_reloader=True)
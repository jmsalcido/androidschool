from flask import render_template, Response
import json
from app import app

@app.route('/places')
@app.route('/places/')
def places_api_stub():
    # used by Android School first event (delete in future)
    places = {
        "places": [
            build_place("nearsoft", 29.0981915, -111.0212922,
                        5, "http://i.imgur.com/k4hESiy.png"),
            build_place("estafeta", 29.0950181, -111.0211799,
                        3, "http://i.imgur.com/vrXKfcd.jpg"),
            build_place("todo empanadas", 29.0922012, -111.0227278,
                        5, "http://i.imgur.com/3MyWjWc.png"),
            build_place("sushi yeye", 29.0913705, -111.0215921,
                        5, "http://i.imgur.com/XzCg1L1.jpg"),
            build_place("plaza conquistador", 29.0942874, -111.0223156,
                        4, "http://i.imgur.com/PUPd1Na.jpg")
        ]
    }
    return Response(json.dumps(places),  mimetype='application/json')


def build_place(name, lat, long, ranking, img_url):
    return {
        "name": name,
        "lat": lat,
        "long": long,
        "ranking": ranking,
        "image_url": img_url
    }

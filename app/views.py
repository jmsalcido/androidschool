from flask import render_template, Response
import json
from app import app


@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')


@app.route('/')
@app.route('/places')
def places_api_stub():
    places = [
        build_place("nearsoft", 29.0981915, -111.0212922, 5),
        build_place("estafeta", 29.0950181, -111.0211799, 3),
        build_place("todo empanadas", 29.0922012, -111.0227278, 5),
        build_place("sushi yeye", 29.0913705, -111.0215921, 5),
        build_place("plaza conquistador", 29.0942874, -111.0223156, 4)
    ]
    return Response(json.dumps(places),  mimetype='application/json')


def build_place(name, lat, long, ranking):
    return {
        name: {
            "lat": lat,
            "long": long,
            "ranking": ranking
        }
    }

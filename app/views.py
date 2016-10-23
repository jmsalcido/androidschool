from flask import render_template, Response, request, jsonify
from flask_security import auth_token_required
from flask_mail import Message
import json
from app import app, mail
from app.send_email import send_email
from app.models import Event, User


@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')


@app.route('/api/events', methods=['GET'])
@app.route('/api/events/', methods=['GET'])
@auth_token_required
def get_events():
    pass

@app.route('/api/email/<email>', methods=['GET'])
@auth_token_required
def email(email_to):
    send_email("Test Subject", "anEmail@fromhere.com", [email_to], "Hola!", "Hola!")


@app.errorhandler(404)
def handle_404(e):
    return app.send_static_file('404.html'), 404


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

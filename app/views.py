from flask import render_template, Response, request, jsonify
from flask_security import auth_token_required
from flask_mail import Message
import json
from app import app, mail
from app.send_email import send_email
from app.models import Event, User
from .deprecated import views
from .api import views

# ===================================
#       GENERAL/PRINCIPAL VIEWS
# ===================================


@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')


@app.errorhandler(404)
def handle_404(e):
    return app.send_static_file('404.html'), 404

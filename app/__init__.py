import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_marshmallow import Marshmallow
from flask_mail import Mail
from app import config

app = Flask(__name__, static_folder='static', static_url_path='')

# configuration load - lazy to load everytime APP_SETTINGS and
# DATABASE_URL in my box.
config_class = os.environ.get('APP_SETTINGS', "app.config.DevelopmentConfig")
app.config.from_object(config_class)

# email
mail = Mail(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app import views, models

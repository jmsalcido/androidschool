import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import config

app = Flask(__name__, static_folder='static', static_url_path='')

# configuration load - lazy to load everytime APP_SETTINGS and
# DATABASE_URL in my box.
config_class = os.environ.get('APP_SETTINGS', "app.config.DevelopmentConfig")
app.config.from_object(config_class)

print(app.config["SECURITY_PASSWORD_HASH"])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import views, models

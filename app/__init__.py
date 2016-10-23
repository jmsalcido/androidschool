from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static', static_url_path='')

# configuration load - lazy to load everytime APP_SETTINGS and DATABASE_URL in my box.
config_class = os.environ['APP_SETTINGS'] if os.environ[
    'APP_SETTINGS'] is not None else "config.DevelopmentConfig"
app.config.from_object(config_class)

from app import views

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

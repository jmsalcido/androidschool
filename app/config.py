import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    QA = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("APP_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    SECRET_KEY = 'aGenericPasswordIsNotWhatYouNeed@1991#000'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'postgresql://localhost/androidschool')
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    QA = True

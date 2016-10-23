import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    QA = False
    CSRF_ENABLED = True
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_SALT = os.environ.get("APP_SECURITY_PASSWORD_SALT")
    SECRET_KEY = os.environ.get("APP_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    SECURITY_PASSWORD_SALT = 'devSalt123'
    SECRET_KEY = 'aGenericPasswordIsNotWhatYouNeed@1991#000'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'postgresql://localhost/androidschool')
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    QA = True

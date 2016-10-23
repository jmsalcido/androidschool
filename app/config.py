import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_SALT = os.environ.get("APP_SECURITY_PASSWORD_SALT")
    SECRET_KEY = os.environ.get("APP_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    WTF_CSRF_ENABLED = False
    DEVELOPER_PASSWORD = os.environ.get('DEVELOPER_PASSWORD')
    # Flask-Security
    SECURITY_USER_IDENTITY_ATTRIBUTES = ['username', 'email']
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'
    SECURITY_LOGIN_URL = '/api/user/login'
    SECURITY_LOGOUT_URL = '/api/user/logout'
    SECURITY_REGISTER_URL = '/api/user/register'
    SECURITY_RESET_URL = '/api/user/reset'
    SECURITY_CHANGE_URL = '/api/user/changepassword'
    SECURITY_RECOVERABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_EMAIL_SUBJECT_REGISTER = 'Welcome to Android School'
    # email
    SENDGRID_API_KEY = os.environ.get('SENDGRIP_API_KEY')
    MAIL_SERVER = os.environ.get('SMTP_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPER_PASSWORD = 'developer'
    SECURITY_PASSWORD_SALT = 'devSalt123'
    SECRET_KEY = 'aGenericPasswordIsNotWhatYouNeed@1991#000'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'postgresql://localhost/androidschool')
    DEVELOPMENT = True
    DEBUG = True
    # email
    SENDGRID_API_KEY = ''
    MAIL_SERVER = 'localhost'
    MAIL_USERNAME = 'developer@localhost'
    MAIL_PASSWORD = 'password'
    MAIL_PORT = 465
    MAIL_USE_SSL = False

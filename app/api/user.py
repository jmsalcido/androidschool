from app import app
from app.send_email import send_email
from itsdangerous import URLSafeTimedSerializer


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token,
                                 salt=app.config['SECURITY_PASSWORD_SALT'],
                                 max_age=expiration)
    except:
        return False
    return email


def send_confirmation_email(email, confirmation_url):
    confirmation_email_text = '''''
Welcome chavo

Please confirm your email:
%s

Thanks!
'''''
    email_text = confirmation_email_text.format(confirmation_url)
    send_email("Confirmation email for Android School", "asd@asd.com", [email], email_text, email_text)

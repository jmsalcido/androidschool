from app import app, db
from .user import generate_confirmation_token
from app.send_email import send_confirmation_email
from app.models import user_datastore, User
from app.ma_schemas import register_schema

from flask import request, jsonify, url_for
from flask_security import auth_token_required
from flask_security.utils import encrypt_password

@app.route('/api/events', methods=['GET'])
@app.route('/api/events/', methods=['GET'])
@auth_token_required
def get_events():
    return "events"

@app.route('/api/user/register', methods=['POST'])
def register():
    data, errors = register_schema.load(request.get_json())
    if errors:
        return jsonify({'errors': errors}), 422
    _user = db.session.query(User).filter(User.username == data.username).first()
    if _user is not None:
        return jsonify({'errors': 'That email address or username is already in the database.'}), 400
    else:
        password_encryped = encrypt_password(data.password)
        user_datastore.create_user(username = data.username,
                                    email = data.email,
                                    password = password_encryped)
        db.session.commit()
        token = generate_confirmation_token(data.email)
        confirmation_url = request.url_root[:-1] + url_for('confirmation', token=token)
        send_confirmation_email(data.email, confirmation_url)
        return jsonify({'data': 'success'}), 201

@app.route('/api/user/confirmation/<token>', methods=['GET'])
def confirmation(token):
    pass

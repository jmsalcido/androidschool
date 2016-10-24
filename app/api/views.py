from app import app, db
from .token import generate_confirmation_token, confirm_token
from app.send_email import send_confirmation_email
from app.models import user_datastore, User
from app.ma_schemas import register_schema

from flask import request, jsonify, url_for
from flask_security import auth_token_required
from flask_security.utils import encrypt_password

from sqlalchemy import or_

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
    _user = User.findFirst(or_(User.username == data.username, User.email == data.email))
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
    try:
        email = confirm_token(token)
    except:
        return jsonify({'error': 'Confirmation link is invalid or has expired'}), 400
    _user = User.findFirst(User.email == email)
    if _user.confirmed_at:
        return jsonify({'error': 'User already confirmed'}), 400
    _user.confirm()
    return jsonify({'data': 'success'}), 201

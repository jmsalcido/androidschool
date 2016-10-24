import os
from app import app, db
from .exceptions import UserNotFoundException
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
from sqlalchemy.orm.exc import NoResultFound


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp())

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('users.id')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('auth_roles.id')))


class Role(Base, RoleMixin):
    __tablename__ = 'auth_roles'
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % self.name


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False,
                         unique=True, index=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(45))
    current_login_ip = db.Column(db.String(45))
    login_count = db.Column(db.Integer)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def all():
        return User.query.all()

    def findFirst(*criterion):
        return User.query.filter(*criterion).first()

    def find(*criterion):
        if criterion:
            try:
                return User.query.filter(*criterion).one()
            except NoResultFound as e:
                raise UserNotFoundException(
                    "No user found with that criterion.")
        return None

    def __repr__(self):
        return '<User %r>' % self.email


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
app.security = Security(app, user_datastore)


class Event(Base):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    start_date = db.Column(db.Date())
    end_date = db.Column(db.Date())
    attendees = db.Column(db.Integer())


@app.before_first_request
def create_user_default_user():
    db.create_all()
    if not User.query.first():
        user_datastore.create_user(username='admin',
                                   email='admin@nearsoft.com',
                                   password=app.config['DEVELOPER_PASSWORD'],
                                   confirmed_at=db.func.current_timestamp())
        db.session.commit()

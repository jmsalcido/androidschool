from app import db, ma
from app.models import User, Event

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = ('username', 'email', 'roles')

class RegisterSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class EventSchema(ma.ModelSchema):
    class Meta:
        model = Event

user_schema = UserSchema()
users_schema = UserSchema(many=True)
register_schema = RegisterSchema()

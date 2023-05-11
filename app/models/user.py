from . import db
from flask_login import UserMixin
import json

class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    given_name = db.Column(db.String(80))
    family_name = db.Column(db.String(80))
    picture = db.Column(db.String(80))
    picture = db.Column(db.String(5))
    identity_provider = db.Column(db.String(80), unique=True)
    identity_id = db.Column(db.String(80), unique=True)
    locale = db.Column(db.String(6), unique=True)
    username = db.Column(db.String(80))
    pwd = db.Column(db.String(300))

    def __repr__(self):
        return "<User %r>" % self.id


def from_oath_google(content) -> User:
    pluck = lambda dict, *args: (dict[arg] for arg in args)
    adict = json.loads(content)
    id, email, name, given_name, family_name, picture, locale = pluck(adict,
        'id', 'email', 'name', 'given_name', 'family_name', 'picture', 'locale')
    return User(identity_provider='google', identity_id=id, username=email, 
                email=email, name=name, given_name=given_name, 
                family_name=family_name, picture=picture, locale=locale)



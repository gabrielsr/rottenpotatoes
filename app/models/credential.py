
from . import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship
from .principal import Principal

from sqlalchemy.ext.declarative import declarative_base


class Credential(db.Model):
    __tablename__ = "credential"
    id = db.Column(db.Integer, primary_key=True)
    principal_id = db.Column(ForeignKey("principal.id"))
    principal: Mapped[Principal] = relationship("Principal", lazy='joined')

    type = db.Column(db.String(20))

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "credential"
    }

class PasswordCredential(Credential):
    password = db.Column(db.String(300))

    __mapper_args__ = {
        "polymorphic_identity": "password"
    }
    def __repr__(self):
        return "<PasswordCredential %r>" % self.id

class OauthCredential(Credential):

    oauth_user_id = db.Column(db.Integer)
    provider = db.Column(db.String(20))
    token = db.Column(db.String(300))

    __mapper_args__ = {
        "polymorphic_identity": "oauth"
    }
    def __repr__(self):
        return f'<OauthCredential { self.oauth_user_id}@{self.provider}>'
    



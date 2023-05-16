from typing import List
from . import db
from sqlalchemy import ForeignKey
from .principal import Principal
from sqlalchemy.orm import Mapped, relationship

class Moviegoer(db.Model):
    __tablename__ = "moviegoers"

    id = db.Column(db.Integer, primary_key=True)
    principal_id = db.Column(db.Integer, ForeignKey(Principal.id), unique=True)
    principal: Mapped[Principal] = relationship(back_populates="me")
    reviews: Mapped[List["Review"]] = relationship(back_populates="moviegoer")
    
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80))
    picture = db.Column(db.String(80))
    bio = db.Column(db.String(300))

    @property
    def username(self):
        if not self.principal:
            return 'not loaded'
        return self.principal.username

    def __repr__(self):
        return "<Moviegoer %r>" % self.username





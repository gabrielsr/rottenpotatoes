from . import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship, Mapped

class Principal(UserMixin, db.Model):
    __tablename__ = "principals"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    me: Mapped["Moviegoer"] = relationship(back_populates="principal")

    def __repr__(self):
        return "<Principal %r>" % self.id


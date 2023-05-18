from sqlalchemy import String
from . import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Principal(UserMixin, db.Model):
    __tablename__ = "principals"

    id:Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), nullable=False)
    me: Mapped["Moviegoer"] = relationship(back_populates="principal") # one-to-one

    def __repr__(self):
        return f'Principal ({self.id}, {self.username})'


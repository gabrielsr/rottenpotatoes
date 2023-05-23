from typing import List, Optional
from . import db
from sqlalchemy import ForeignKey, String
from .principal import Principal
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Moviegoer(db.Model):
    __tablename__ = "moviegoers"

    id:Mapped[int] = mapped_column(primary_key=True)
    principal_id:Mapped[int] = mapped_column(ForeignKey(Principal.id), unique=True) #*one-to-one
    principal: Mapped[Principal] = relationship(back_populates="me")
    
    reviews: Mapped[list["Review"]] = relationship(back_populates="moviegoer") # one-to-*many
    
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(80))
    picture: Mapped[Optional[str]] = mapped_column(String(80))
    bio: Mapped[Optional[str]] = mapped_column(String(300))

    movies: Mapped[list["Movie"]] = relationship("Movie", secondary="reviews") # *many-to-many

    @property
    def username(self):
        if not self.principal:
            return 'not loaded'
        return self.principal.username

    def __repr__(self):
        return f'Moviegoer ({self.id}, {self.name}, {self.email})'





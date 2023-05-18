from sqlalchemy import CheckConstraint, ForeignKey, Integer, orm
from . import db
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .movie import Movie
from .moviegoer import Moviegoer

class Review(db.Model):
    __tablename__ = "reviews"

    id:Mapped[int] =    mapped_column(primary_key=True)
    movie_id:Mapped[int] = mapped_column(ForeignKey("movies.id"), index=True)
    moviegoer_id:Mapped[int] = mapped_column(ForeignKey("moviegoers.id")) 
    movie: Mapped["Movie"] = relationship(back_populates="reviews")  #one-to-*many
    moviegoer: Mapped["Moviegoer"] = relationship(back_populates="reviews") #one-to-*many
    potatoes:Mapped[int] = mapped_column(Integer, CheckConstraint('potatoes > 0 AND potatoes <= 5'))

    @orm.validates('potatoes')
    def validate_potatoes_range(self, key, value):
        if not 0 < value <= 5:
            raise ValueError(f'Invalid potatoes {value}')
        return value

    @property
    def moviegoer_name(self):
        return self.moviegoer.name
    
    def __repr__(self):
        return f'Review ({self.id}, {self.movie_id}, {self.moviegoer_id}, {self.potatoes})'


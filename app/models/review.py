from . import db
from sqlalchemy.orm import relationship, Mapped
from .movie import Movie
from .moviegoer import Moviegoer

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"), nullable=False)
    moviegoer_id = db.Column(db.Integer, db.ForeignKey("moviegoers.id"), nullable=False)
    movie: Mapped["Movie"] = relationship(Movie, back_populates="reviews")
    moviegoer: Mapped["Moviegoer"] = relationship(Moviegoer, back_populates="reviews")
    potatoes = db.Column(db.Integer, nullable=False)

    @property
    def moviegoer_name(self):
        return self.moviegoer.name
    
    def __repr__(self):
        return "<Review %r>" % self.id


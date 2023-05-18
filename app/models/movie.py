from datetime import datetime
from typing import Optional
from . import db
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Movie(db.Model):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(64))
    rating: Mapped[str] = mapped_column(String(6))
    description: Mapped[str] = mapped_column(String(256))
    release_date: Mapped[Optional[datetime]] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow, onupdate=datetime.utcnow)
    reviews:  Mapped[list["Review"]] = relationship(back_populates="movie")

    def __repr__(self):
        return f'Movie ({self.id}, {self.title}, {self.rating}, {self.release_date})'

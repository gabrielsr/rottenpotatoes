from flask.cli import AppGroup

from .webapp import db
from .models import Movie, Moviegoer, Review, PasswordCredential, Principal
from .seed import movies, moviegoers, reviews, credentials, principals

seed_cli = AppGroup("seed")


@seed_cli.command("movies")
def seed_movies():
    "Add seed data to the database."
    for movie in movies:
        db.session.add(Movie(**movie))

@seed_cli.command("reviews")
def seed_reviews():
    for review in reviews:
        db.session.add(Review(**review))
    db.session.commit()


@seed_cli.command("users")
def seed_users():
    "Add seed data to the database."
    for p in principals:
        db.session.add(Principal(**p))
    for m in moviegoers:
        db.session.add(Moviegoer(**m))
    for c in credentials:
        db.session.add(PasswordCredential(**c))

    db.session.commit()


@seed_cli.command("all")
def seed_all():
    "Add seed data to the database."
    seed_movies()
    seed_users()
    seed_reviews()
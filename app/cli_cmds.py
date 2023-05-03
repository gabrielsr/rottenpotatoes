import click

from flask.cli import AppGroup
from .webapp import db
from .models import Movie
from .seed import movies

admin_cli = AppGroup("admin")


@admin_cli.command("seed")
# @click.argument("name")
def seed():
    print("seeding database")
    "Add seed data to the database."
    for movie in movies:
        db.session.add(Movie(**movie))
    db.session.commit()

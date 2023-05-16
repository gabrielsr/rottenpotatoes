from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

from app.helpers.form_view import form_edit_view, form_validated, form_view, load_parent_resource_factory
from app.helpers.standard_paths import get_standard_template_paths
from app.models.movie import Movie

from ..models import Review
# from .movies_controllers import bp as movies_bp

bp_name = "reviews"

tmpl = get_standard_template_paths(bp_name)

bp = Blueprint(bp_name, __name__)
modelcls = Review
pmodelcls = Movie
properties = {
    "entity_name": "review",
    "collection_name": "Reviews",
    "list_fields": ["potatoes", "moviegoer_name"],
}

def register_blueprint(parent_blueprint: Blueprint):
    parent_blueprint.register_blueprint(bp, url_prefix=f"/<int:movie_id>/reviews")

load_parent = load_parent_resource_factory(pmodelcls, "movie_id")


@bp.route("/", methods=["GET"])
@load_parent
def index(movie: Movie):
    """
    Index page.
    :return: The list of reviews of a movie.
    """
    reviews = movie.reviews
    return render_template(tmpl.index, entities=reviews, **properties)

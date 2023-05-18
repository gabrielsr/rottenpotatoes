from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from wtforms import SubmitField, HiddenField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, NumberRange

from app.helpers.form_view import form_edit_view, form_validated, form_view, load_parent_resource_factory
from app.helpers.standard_paths import get_standard_template_paths
from app.models.movie import Movie
from ..models import Review

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


class _j:
    index = f"{bp_name}/index.jinja2"


def register_blueprint(parent_blueprint: Blueprint):
    parent_blueprint.register_blueprint(
        bp, url_prefix=f"/<int:movie_id>/reviews")


load_parent = load_parent_resource_factory(pmodelcls, "movie_id")
from ..webapp import db

@bp.route("/", methods=["GET"])
@load_parent
def index(movie: Movie):
    """
    Index page.
    :return: The list of reviews of a movie.
    """
    reviews = movie.reviews
    return render_template(tmpl.index, entities=reviews, **properties)

@bp.route("/<int:review_id>/show", methods=["GET"])
def show(movie_id:int, review_id: int):
    """
    Show page.
    :return: The response.
    """
    review = db.get_or_404(Review, review_id)
    return render_template(tmpl.show, entity=review, **properties)

class ReviewForm(FlaskForm):
    movie_id = HiddenField()
    potatoes = IntegerField("Potatoes", validators=[
                            InputRequired(), NumberRange(min=1, max=5)])
    submit = SubmitField("Submit")


@bp.route("/new", methods=["GET"])
@login_required
@form_view(ReviewForm)
def new(form: ReviewForm, movie_id: int):
    """
    Page to create new Entity
    :return: render create template
    """
    return render_template(tmpl.new, form=form, **properties)


@bp.route("/", methods=["POST"])
@load_parent
@form_validated(ReviewForm, new)
def create(form: ReviewForm, movie: Movie):
    """
    Create new entity
    If form is valid, create new entity and redirect to show page
    If form is not valid, render new template with errors

    :return: redirect to view new entity
    """
    newreview = Review(moviegoer_id=current_user.id)
    form.populate_obj(newreview)
    db.session.add(newreview)
    db.session.commit()
    flash(f"'Review for { newreview.movie.title}' created")
    return redirect(url_for('.index', movie_id=movie.id))



@bp.route("/<int:review_id>/edit", methods=["GET"])
@form_edit_view(ReviewForm, entitycls=Review, id_key='review_id')
def edit(form: ReviewForm, movie_id:int, review_id: int):
    """
    Edit page.
    :return: The response.
    """
    return render_template(tmpl.edit, form=form,  movie_id=movie_id, review_id=review_id, **properties)


#@bp.route("/<int:id>", methods=["UPDATE"])
@bp.route("/<int:review_id>/edit", methods=["POST"])
@form_validated(ReviewForm, edit)
def update(form: ReviewForm, movie_id:int, review_id:int):
    """
    Save Edited Entity
    If form is valid, update entity and redirect to show page
    If form is not valid, render edit template with errors
    :return: redirect to show entity
    """
    entity = db.get_or_404(Review, review_id)
    form.populate_obj(entity)
    db.session.add(entity)
    db.session.commit()
    flash(f"'Review of movie { movie_id}' updated")
    return redirect(url_for('.show', movie_id=movie_id, review_id=review_id))


#@bp.route("/<int:id>", methods=["DELETE"])
@bp.route("/<int:review_id>/delete", methods=["POST"])
def destroy(movie_id:int, review_id:int):
    """
    Delete Entity
    :return: redirect to list
    """
    review = db.get_or_404(Review, review_id)
    db.session.delete(review)
    db.session.commit()
    flash(f"Review '{ review_id}' deleted")
    return redirect(url_for('.index', movie_id=movie_id))

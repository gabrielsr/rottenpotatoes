from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

from app.helpers.form_view import form_edit_view, form_validated, form_view
from app.helpers.standard_paths import get_standard_template_paths

from ..models import Movie

from .reviews_controller import register_blueprint as register_reviews_blueprint

bp_name = "movies"

bp = Blueprint(bp_name, __name__)
register_reviews_blueprint(bp)

from ..webapp import db

properties = {
    "entity_name": "movie",
    "collection_name": "Movies",
    "list_fields": ["title", "rating", "description"],
}


class _to:
    def __to(method):
        return lambda **kwargs: url_for(f"{bp_name}.{method}", **kwargs)

    index = __to("index")
    show = __to("show")
    edit = __to("edit")
    delete = __to("delete")


tmpl = get_standard_template_paths(bp_name)

@bp.route("/", methods=["GET"])
def index():
    """
    Index page.
    :return: The response.
    """
    movies = Movie.query.all()
    return render_template(tmpl.index, entities=movies, **properties)



@bp.route("/<int:id>/show", methods=["GET"])
def show(id: int):
    """
    Show page.
    :return: The response.
    """
    movie = db.get_or_404(Movie, id)
    return render_template(tmpl.show, entity=movie, **properties)

class MovieForm(FlaskForm):
    title = StringField("title", validators=[InputRequired()])
    rating = StringField("rating")
    description = StringField("description")
    submit = SubmitField("Submit")


@bp.route("/new", methods=["GET"])
@login_required
@form_view(MovieForm)
def new(form: MovieForm):
    """
    Page to create new Entity
    :return: render create template
    """
    return render_template(tmpl.new, form=form, **properties)


@bp.route("/", methods=["POST"])
@form_validated(MovieForm, new)
def create(form: MovieForm):
    """
    Create new entity
    If form is valid, create new entity and redirect to show page
    If form is not valid, render new template with errors

    :return: redirect to view new entity
    """
    newmovie = Movie()
    form.populate_obj(newmovie)
    db.session.add(newmovie)
    db.session.commit()
    flash(f"'{ newmovie.title}' created")
    return redirect(url_for('.show', id=newmovie.id))


@bp.route("/<int:id>/edit", methods=["GET"])
@form_edit_view(MovieForm, entitycls=Movie)
def edit(form: MovieForm, id: int):
    """
    Edit page.
    :return: The response.
    """
    return render_template(tmpl.edit, form=form, **properties)


# @bp.route("/<int:id>", methods=["UPDATE"])
@bp.route("/<int:id>/edit", methods=["POST"])
@form_validated(MovieForm, edit)
def update(form: MovieForm, id: int):
    """
    Save Edited Entity
    If form is valid, update entity and redirect to show page
    If form is not valid, render edit template with errors
    :return: redirect to show entity
    """
    movie = db.get_or_404(Movie, id)
    form.populate_obj(movie)
    db.session.commit()
    flash(f"'{ movie.title}' updated")
    return redirect(url_for('.show', id=id))


# @bp.route("/<int:id>", methods=["DELETE"])
@bp.route("/<int:id>/delete", methods=["POST"])
def destroy(id: int):
    """
    Delete Entity
    :return: redirect to list
    """
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    flash(f"'{ movie.title}' deleted")
    return redirect(url_for('.index'))

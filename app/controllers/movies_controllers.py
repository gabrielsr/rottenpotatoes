from flask import Blueprint, render_template, request, redirect, url_for, flash
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

from ..models import Movie

bp_name = "movies"

bp = Blueprint(bp_name, __name__)
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


class _j:
    index = f"{bp_name}/index.jinja2"
    edit = f"{bp_name}/edit.jinja2"
    show = f"{bp_name}/show.jinja2"
    new = f"{bp_name}/new.jinja2"
    create = f"{bp_name}/create.jinja2"
    search_tmdb = f"{bp_name}/search_tmdb.jinja2"


@bp.route("/", methods=["GET"])
def index():
    """
    Index page.
    :return: The response.
    """
    movies = Movie.query.all()
    return render_template(_j.index, entities=movies, **properties)


class EditForm(FlaskForm):
    title = StringField("title", validators=[InputRequired()])
    rating = StringField("rating")
    description = StringField("description")
    submit = SubmitField("Submit")


@bp.route("/new", methods=["GET"])
def new():
    """
    Page to create new Entity
    :return: render create template
    """
    form = EditForm()
    return render_template(_j.new, form=form, **properties)


@bp.route("/", methods=["POST"])
def create():
    """
    Create new entity
    :return: redirect to view new entity
    """
    form = EditForm(formdata=request.form)
    if form.validate_on_submit():
        newmovie = Movie()
        form.populate_obj(newmovie)
        db.session.add(newmovie)
        db.session.commit()
        flash(f"'{ newmovie.title}' created")
        return redirect(_to.show(id=newmovie.id))
    else:
        flash("Error in form validation", "danger")


@bp.route("/<int:id>/show", methods=["GET"])
def show(id):
    """
    Show page.
    :return: The response.
    """
    movie = db.get_or_404(Movie, id)
    return render_template(_j.show, entity=movie, **properties)


@bp.route("/<int:id>/edit", methods=["GET"])
def edit(id):
    """
    Edit page.
    :return: The response.
    """
    movie = db.get_or_404(Movie, id)
    userform = EditForm(formdata=request.form, obj=movie)
    return render_template(_j.edit, form=userform, **properties)


@bp.route("/<int:id>/edit", methods=["POST", "UPDATE"])
@bp.route("/<int:id>", methods=["UPDATE"])
def update(id):
    """
    Save Edited Entity
    :return: redirect to show entity
    """
    movie = db.get_or_404(Movie, id)
    form = EditForm(formdata=request.form, obj=movie)
    if form.validate_on_submit():
        form.populate_obj(movie)
        db.session.commit()
        flash(f"'{ movie.title}' updated")
        return redirect(_to.show(id=id))
    else:
        flash("Error in form validation", "danger")


@bp.route("/<int:id>/delete", methods=["POST", "DELETE"])
def destroy(id):
    """
    Delete Entity
    :return: redirect to list
    """
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    flash(f"'{ movie.title}' deleted")
    return redirect(_to.index())

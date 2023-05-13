from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

from ..models import Moviegoer

bp_name = "moviegoers"

bp = Blueprint(bp_name, __name__)
from ..webapp import db


properties = {
    "entity": "moviegoer",
    "title": "Moviegoers",
    "list_fields": ["id", "username", "email"],
}


class _to:
    def __to(method):
        return lambda: url_for(f"{bp_name}.{method}")

    index = __to("index")
    edit = __to("edit")
    delete = __to("delete")


class _j:
    index = f"{bp_name}/index.jinja2"
    edit = f"{bp_name}/edit.jinja2"


@bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    """
    Index page.
    :return: The response.
    """
    users = Moviegoer.query.all()
    return render_template(_j.index, entities=users, **properties)


class EditForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    submit = SubmitField("Submit")


@bp.route("/<int:id>/edit", methods=["GET"])
@login_required
def edit(id):
    """
    Edit page.
    :return: The response.
    """
    entity = db.get_or_404(Moviegoer, id)
    form = EditForm(obj=entity)
    return render_template(_j.edit, form=form, **properties)


@bp.route("/<int:id>/edit", methods=["POST"])
@login_required
def update(id):
    """
    Save Edited Entity
    :return: redirect to list
    """
    form = EditForm()
    if form.validate_on_submit():
        entity = db.get_or_404(Moviegoer, id)
        form.populate_obj(entity)
        db.session.commit()
        return redirect(_to.index())
    else:
        flash("Error in form validation", "danger")


@bp.route("/<int:id>/delete", methods=["POST"])
@login_required
def destroy(id):
    """
    Delete Entity
    :return: redirect to list
    """
    obj = Moviegoer.query.filter_by(id=id).one()
    db.session.delete(obj)
    db.session.commit()
    flash("Entry deleted")
    return redirect(_to.index())

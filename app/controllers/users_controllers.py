from flask import Blueprint, render_template, request, redirect, url_for, flash
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

from ..models import User

bp_name = "users"

bp = Blueprint(bp_name, __name__)
from ..webapp import db


properties = {
    "entity": "user",
    "title": "Users",
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
def index():
    """
    Index page.
    :return: The response.
    """
    users = User.query.all()
    return render_template(_j.index, entities=users, **properties)


class EditForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    submit = SubmitField("Submit")


@bp.route("/<int:id>/edit", methods=["GET"])
def edit(id):
    """
    Edit page.
    :return: The response.
    """
    user = db.get_or_404(User, id)
    userform = EditForm(formdata=request.form, obj=user)

    form = EditForm(obj=user)
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(_to.index())

    return render_template(_j.edit, form=userform, **properties)


@bp.route("/<int:id>/edit", methods=["POST"])
def do_edit(id):
    """
    Save Edited Entity
    :return: redirect to list
    """
    form = EditForm()
    if form.validate_on_submit():
        user = db.get_or_404(User, id)
        form.populate_obj(user)
        db.session.commit()
        return redirect(_to.index())
    else:
        flash("Error in form validation", "danger")


@bp.route("/<int:id>/delete", methods=["POST"])
def delete(id):
    """
    Delete Entity
    :return: redirect to list
    """
    obj = User.query.filter_by(id=id).one()
    db.session.delete(obj)
    db.session.commit()
    flash("Entry deleted")
    return redirect(_to.index())

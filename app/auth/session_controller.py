from flask import render_template, redirect, url_for
from flask import Blueprint

from flask_login import (
    logout_user,
    login_required,
)

from app.helpers.form_view import form_view

from .forms import login_form
from flask_wtf import FlaskForm

bp = Blueprint("session", __name__)


@bp.route("/login", methods=["GET"], strict_slashes=False)
@form_view(login_form)
def login(form: FlaskForm):
    return render_template("auth/login.jinja2", form=form)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.session.login"))


from functools import wraps
from flask import render_template, redirect, flash, url_for
from flask import Blueprint

from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required,
)

from app.helpers.form_view import form_view, form_validated, get_form_data

from .forms import login_form, register_form
from .register_service import register_with_pwd
from flask_wtf import FlaskForm
from .session_controller import login as login_view

bp = Blueprint("passwd", __name__)




@bp.route("/login", methods=["POST"], strict_slashes=False)
@form_validated(login_form, login_view)
def check_credentials(form):
    login_user(form.principal.data)
    flash("Logged in successfully.", "success")
    return redirect(url_for("main.index"))


@bp.route("/register/", methods=["GET"], strict_slashes=False)
@form_view(register_form)
def register(form):
    return render_template(
        "auth/register.jinja2",
        form=form,
        text="Create account",
        title="Register",
        btn_action="Register account",
    )


@bp.route("/register/", methods=["POST"], strict_slashes=False)
@form_validated(register_form, register)
def create(form):
    try:
        kwargs = get_form_data(form, "username", "password", "email")
        principal = register_with_pwd(**kwargs)
        login_user(principal)
        flash(f"Account Succesfully created", "success")
        return redirect(url_for("home"))

    except Exception as e:
        flash(f"Failed to create account {e}", "danger")

    return register(form)

@bp.route("/reset-password")
def forgot():
    raise NotImplementedError
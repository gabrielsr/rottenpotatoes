from functools import wraps
from flask import render_template, redirect, flash, url_for
from flask import Blueprint

from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required,
)

from app.helpers.form_view import FormGeneralError, form_view, form_validated, get_form_data

from .forms import login_form, register_form
from .register_service import check_pwd_credential, register_with_pwd
from flask_wtf import FlaskForm

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET"], strict_slashes=False)
@form_view(login_form)
def login(form: FlaskForm):
    return render_template("auth/login.jinja2", form=form)

@bp.route("/login", methods=["POST"], strict_slashes=False)
@form_validated(login_form, login)
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


@bp.route("/profile/", methods=["GET"], strict_slashes=False)
@login_required
def profile():
    me = current_user.me
    return render_template("auth/profile.jinja2", profile=me)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@bp.route("/reset-password")
def forgot_password():
    raise NotImplementedError
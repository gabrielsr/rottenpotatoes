from flask import render_template, redirect, flash, url_for, session

from datetime import timedelta
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)
from werkzeug.routing import BuildError


from flask_bcrypt import check_password_hash

from flask_login import (
    login_user,
    logout_user,
    login_required,
)

from ..webapp import db, bcrypt
from ..models import User
from .forms import login_form, register_form


from . import bp


@bp.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("index.jinja2", title="Home")


@bp.route("/login/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    if form.validate_on_submit():
        try:
            user = User.query.filter_by(username=form.username.data).first()
            if user is None:
                # In production, it is recommended to use a generic message
                flash("User not found", "danger")
            elif check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
                return redirect(url_for("main.index"))
            else:
                flash("Invalid Username or password!", "danger")
        except Exception as e:
            flash(e, "danger")

    return render_template("auth/login.jinja2", form=form)


@bp.route("/profile/", methods=("GET", "POST"), strict_slashes=False)
def profile():
    return render_template("auth/profile.jinja2")


# Register route
@bp.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = register_form()
    if form.validate_on_submit():
        try:
            email = form.email.data
            pwd = form.pwd.data
            username = form.username.data

            newuser = User(
                username=username,
                email=email,
                pwd=bcrypt.generate_password_hash(pwd),
            )

            db.session.add(newuser)
            db.session.commit()
            flash(f"Account Succesfully created", "success")
            return redirect(url_for("login"))

        except InvalidRequestError:
            db.session.rollback()
            flash(f"Something went wrong!", "danger")
        except IntegrityError:
            db.session.rollback()
            flash(f"User already exists!.", "warning")
        except DataError:
            db.session.rollback()
            flash(f"Invalid Entry", "warning")
        except InterfaceError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except DatabaseError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except BuildError:
            db.session.rollback()
            flash(f"An error occured !", "danger")
    return render_template(
        "auth/register.jinja2",
        form=form,
        text="Create account",
        title="Register",
        btn_action="Register account",
    )


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

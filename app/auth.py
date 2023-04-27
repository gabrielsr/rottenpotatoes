import functools
from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

bp = Blueprint("auth", __name__)
from .models import db


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = db.execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


class RegisterForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])
    submit_button = SubmitField("Submit This Form")


@bp.route("/register", methods=("GET", "POST"))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for("auth.login"))
    else:
        print(form.name.username)

        return render_template("auth/register.html", form=form)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        # db = get_db()
        # if error is None:
        #     try:
        #         db.execute(
        #             "INSERT INTO user (username, password) VALUES (?, ?)",
        #             (username, generate_password_hash(password)),
        #         )
        #         db.commit()
        #     except db.IntegrityError:
        #         error = f"User {username} is already registered."
        #     else:
        #         return redirect(url_for("auth.login"))

        flash(error)
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


class LoginForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])
    submit_button = SubmitField("Submit This Form")


@bp.route("/login", methods=("GET", "POST"))
def login():
    form = RegisterForm()
    if form.validate_on_submit():
        username = request.form["username"]
        password = request.form["password"]
        error = None

        # db = get_db()
        # user = db.execute(
        #     "SELECT * FROM user WHERE username = ?", (username,)
        # ).fetchone()
        user = {"password": "password"}
        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

        flash(error, "danger")
        return redirect(url_for("main.index"))
    else:
        return render_template("auth/login.html", form=form)


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

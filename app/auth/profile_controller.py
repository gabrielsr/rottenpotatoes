
from flask import render_template
from flask import Blueprint

from flask_login import (
    current_user,
    login_required,
)

bp = Blueprint("profile", __name__)


@bp.route("/me", methods=["GET"], strict_slashes=False)
@login_required
def me():
    me = current_user.me
    return render_template("auth/profile.jinja2", profile=me)
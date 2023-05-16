
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from .oauth_controller import ggbp as googlebp
from .oauth_controller import ghbp as githubbp
from .pwd_auth_controller import bp as passwdbp
from .session_controller import bp as sessionbp
from .profile_controller import bp as profilebp

auth_bp.register_blueprint(sessionbp)
auth_bp.register_blueprint(googlebp)
auth_bp.register_blueprint(githubbp)
auth_bp.register_blueprint(passwdbp, url_prefix=f"/passwd")
auth_bp.register_blueprint(profilebp, url_prefix=f"/profile")

__all__ = [auth_bp]
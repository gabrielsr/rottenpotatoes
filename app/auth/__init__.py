from flask import Blueprint
from .oath_google import google_blueprint
bp = Blueprint("auth", __name__)
oath_blueprints = [google_blueprint]

from .controller import *

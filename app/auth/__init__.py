from flask import Blueprint
from .oath import google_blueprint
bp = Blueprint("auth", __name__)
oath_blueprints = [google_blueprint]

from .controller import *

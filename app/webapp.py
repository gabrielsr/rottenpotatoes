import os

basedir = os.path.abspath(os.path.dirname(__file__))

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

# init extensions
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
bootstrap = Bootstrap5()


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )
    app.config.from_prefixed_env()

    # app.config.from_pyfile(config_filename)

    # from yourapplication.views.admin import admin
    # from yourapplication.views.frontend import frontend
    # app.register_blueprint(admin)
    # app.register_blueprint(frontend)

    # # WEBSITE_HOSTNAME exists only in production environment
    # if 'WEBSITE_HOSTNAME' not in os.environ:
    #     # local development, where we'll use environment variables
    #     print("Loading config.development and environment variables from .env file.")
    #     app.config.from_object('azureproject.development')
    # else:
    #     # production
    #     print("Loading config.production.")
    #     app.config.from_object('azureproject.production')

    # configure the SQLite database, relative to the app instance folder
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    app.secret_key = "secret-key"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    # init extensions
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    # register blueprints
    from .auth import bp as auth_bp

    app.register_blueprint(auth_bp)

    from .controllers import blueprints

    for bp in blueprints():
        app.register_blueprint(bp, url_prefix=f"/{bp.name}")

    # initialize the app with the extension

    # app.secret_key = "super secret string"  # Change this!
    # print("!!! print change the secret key !!!")

    from .auth.loaders import load_user

    # initialize commands
    from .cli_cmds import seed_cli

    app.cli.add_command(seed_cli)

    return app


app = create_app()

"""
404 Page not found error default handler
"""


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/404.jinja2", error=e), 404


# @app.get("/")
# def index():
#     return render_template("index.jinja2")

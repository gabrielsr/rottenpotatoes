from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from .config import get_config

# init extensions
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.session.login"
login_manager.login_message_category = "info"
db:SQLAlchemy = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
bootstrap = Bootstrap5()

# config manager
config = get_config()

def create_app():
    app = Flask(__name__)
    # load config
    app.config.from_object(config)

    # init extensions
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    # register flask blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix=f"/{auth_bp.name}")

    from .controllers import blueprints

    for bp in blueprints():
        app.register_blueprint(bp, url_prefix=f"/{bp.name}")

    # register api blueprint 
    from .api import blueprint as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')


    from .auth.loaders import load_user
    # from .models import Moviegoer, PasswordCredential
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


@app.get("/")
def home():
    return render_template("index.jinja2")

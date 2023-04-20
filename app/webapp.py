from flask import Flask


def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile(config_filename)

    # from yourapplication.model import db
    # db.init_app(app)

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

    return app


app = create_app()


@app.get("/")
def index():
    return "Hello World"

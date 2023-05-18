import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key") # In production, should be set to a random string
    GOOGLE_OAUTH_CLIENT_ID =  os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
    GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
    GITHUB_OAUTH_CLIENT_ID = os.environ.get("GITHUB_OAUTH_CLIENT_ID")
    GITHUB_OAUTH_CLIENT_SECRET = os.environ.get("GITHUB_OAUTH_CLIENT_SECRET")
    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO", False ) # Print in console all SQL commands


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", 'mysql://user@localhost/foo')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(Config):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True


config_map = {
    "development":  DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}

def get_env():
    if os.getenv("APP_ENV") == "production":
        return "production"
    elif os.getenv("APP_ENV") == "testing":
        return "testing"
    else:
        return "development"
    
def get_config() -> Config:
    print("!!! init config !!!")
    env = get_env()
    print(f"!!! env: {env} !!!")
    return config_map[env]
    # get config environment from environment variable, default to development
   
    
    


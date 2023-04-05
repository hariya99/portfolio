# to make it a package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Environment 
TEST = True

# this has to be below TEST to avoid circular import issue 
from backend.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    """
        This function will help create multiple instances of 
        the application. So, scaling it up will be easy
    """
    # name of the module
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from backend.home.routes import home
    app.register_blueprint(home)

    return app


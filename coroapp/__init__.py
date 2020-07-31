from flask import Flask
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    

    from coroapp import routes
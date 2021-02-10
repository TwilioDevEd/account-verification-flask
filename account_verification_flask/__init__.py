from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from account_verification_flask.config import config_env_files

app = Flask(__name__)
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def prepare_app(
    environment='development', p_db=db, p_bcrypt=bcrypt, p_login_manager=login_manager
):
    app.config.from_object(config_env_files[environment])

    p_db.init_app(app)
    p_bcrypt.init_app(app)
    p_login_manager.init_app(app)
    p_login_manager.login_view = 'register'
    return app


prepare_app()

import account_verification_flask.views  # noqa F402

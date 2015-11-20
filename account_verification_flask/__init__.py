from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from account_verification_flask.config import config_env_files

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_name):
    new_app = Flask(__name__)
    new_app.config.from_object(config_env_files['default'])

    if not config_name == 'default':
        new_app.config.from_object(config_env_files[config_name])
        
    new_app.config.from_object(config_env_files['local'])
    db.init_app(new_app)
    bcrypt.init_app(new_app)
    login_manager.init_app(new_app)
    login_manager.login_view = 'register'
    return new_app
    

app = create_app('default')

import account_verification_flask.views
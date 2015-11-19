from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt


app = Flask(__name__)

app.config.from_object('account_verification_flask.defaults')
app.config.from_envvar('ACCOUNT_VERIFICATION_SETTINGS')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'register'

bcrypt = Bcrypt(app)


import account_verification_flask.views
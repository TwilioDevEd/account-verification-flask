from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = '!^%@*!&$852438#(&^874@#^&*($@*(@&^@)(&*)Y_)((+'
app.config['AUTHY_KEY'] = 'fdfdfdfdfdfdfd'

app.config['TWILIO_ACCOUNT_SID'] = 'bla'
app.config['TWILIO_AUTH_TOKEN'] = 'bla'
app.config['TWILIO_NUMBER'] = 'bla'

# Create in-memory database
app.config['DATABASE_FILE'] = 'D:\\WORK\\account_verification.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'register'

bcrypt = Bcrypt(app)


import account_verification_flask.views
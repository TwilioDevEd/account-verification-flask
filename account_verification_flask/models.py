#from flask.ext.login import UserMixin
from account_verification_flask import db, bcrypt
from .utils import ensure_utf

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    phone_number = db.Column(db.String, nullable=False)
    country_code = db.Column(db.String, nullable=False)
    phone_number_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    authy_user_id = db.Column(db.String, nullable=True)

    def __init__(self, name, email, password, phone_number, country_code):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.phone_number = phone_number
        self.country_code = country_code
        self.phone_number_confirmed =  False;

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
        
    def confirm_phone_number(self):
        self.phone_number_confirmed =  True

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<User %r>' % (self.name)
            
        
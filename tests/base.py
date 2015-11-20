from flask.ext.testing import TestCase
import account_verification_flask
from account_verification_flask import app, db, create_app
from account_verification_flask.models.models import *


class BaseTestCase(TestCase):
    
    def create_app(self):
        app = create_app('test')
        app.config['TESTING'] = True
        return app


    #def setUp(self):
        


    #def setUp(self):
    #    db.create_all()
    #    db.session.add(User("admin", "ad@min.com", "admin"))
    #    db.session.commit()

    #def tearDown(self):
    #    db.session.remove()
    #    db.drop_all()
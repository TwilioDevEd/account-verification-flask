from account_verification_flask import app
from flask_testing import TestCase


class BaseTestCase(TestCase):
    def create_app(self):
        return app

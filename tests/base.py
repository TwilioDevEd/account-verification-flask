﻿from account_verification_flask import app
from flask.ext.testing import TestCase


class BaseTestCase(TestCase):
    render_templates = False

    def create_app(self):
        return app

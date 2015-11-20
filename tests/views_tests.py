import unittest

from flask.ext.login import current_user
from flask import request

from base import BaseTestCase


class ViewsTests(BaseTestCase):
    render_templates = False

    # Ensures /verify renders the correct view
    def test_verify_registration_code_action_renders_default_view(self):
        response = self.client.get('/verify')
        self.assert_template_used('verify_registration_code.html')

    ## Ensure that main page requires user login
    #def test_main_route_requires_login(self):
    #    response = self.client.get('/', follow_redirects=True)
    #    self.assertIn(b'Please log in to access this page', response.data)



if __name__ == '__main__':
    unittest.main()   
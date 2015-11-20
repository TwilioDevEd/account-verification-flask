import unittest
from flask.ext.login import current_user
from flask import request, url_for
from flask.testing import FlaskClient
from base import BaseTestCase

class ViewsTests(BaseTestCase):
    
    # Ensures rout '/' renders the correct view
    def test_index_action_renders_default_view(self):
        # act
        response = self.client.get('/')

        # assert
        self.assert_template_used('index.html')

    # Ensures route '/verify' renders the correct view
    def test_verify_registration_code_action_renders_default_view(self):
        # act
        response = self.client.get('/verify')

        # assert
        self.assert_template_used('verify_registration_code.html')

    # Ensures route '/resend' renders the correct view
    def test_resend_registration_code_action_renders_default_view(self):
        # act
        response = self.client.get('/resend')

        # assert
        self.assert_template_used('resend_confirmation_code.html')

    # Ensures route '/status' renders the correct view
    def test_status_action_renders_default_view(self):
        # act
        response = self.client.get('/status')

        # assert
        self.assert_template_used('status.html')

    ## Ensures /status renders the correct view
    #def test_register_redirects_to_verifiy_view(self):
    #    response = self.client.post('/register', 
    #                                data=dict(name="name", 
    #                                     email="user@email.com", 
    #                                     password="password",
    #                                     country_code="1",
    #                                     phone_number="54654646464"),
    #                                follow_redirects=True)

    #    #assert response.request.path == url_for('verify', email="user@email.com"))
    #    self.assertRedirects(response,url_for('verify', email="user@email.com"))

if __name__ == '__main__':
    unittest.main()   
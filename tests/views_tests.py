import unittest

from .base import BaseTestCase


class ViewsTests(BaseTestCase):

    # Ensures rout '/' renders the correct view
    def test_index_action_renders_default_view(self):
        # act
        self.client.get('/')

        # assert
        self.assert_template_used('index.html')

    # Ensures route '/verify' renders the correct view
    def test_verify_registration_code_action_renders_default_view(self):
        # act
        self.client.get('/verify')

        # assert
        self.assert_template_used('verify_registration_code.html')

    # Ensures route '/resend' renders the correct view
    def test_resend_registration_code_action_renders_default_view(self):
        # act
        self.client.get('/resend')

        # assert
        self.assert_template_used('resend_confirmation_code.html')

    # Ensures route '/status' renders the correct view
    def test_status_action_renders_default_view(self):
        # act
        self.client.get('/status')

        # assert
        self.assert_template_used('status.html')


if __name__ == '__main__':
    unittest.main()

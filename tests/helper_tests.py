import unittest

from account_verification_flask.utilities.view_helpers import redirect_to, view
from .base import BaseTestCase
from flask import redirect, url_for, render_template


class ViewHelperTests(BaseTestCase):
    def test_redirect_to_redirects_to_same_location_of_redirect(self):
        """
        Ensures 'redirect_to' redirect you to the same place as 'redirect'
        """
        # assert
        self.assertEqual(
            redirect_to('home').location, redirect(url_for('home')).location
        )

    def test_redirect_to_redirects_to_same_location_of_redirect_with_route_params(self):
        """
        Ensures 'redirect_to' redirect you to the same place as 'redirect'
        with routes params
        """
        # assert
        self.assertEqual(
            redirect_to('verify', email="user@email.com").location,
            redirect(url_for('verify', email="user@email.com")).location,
        )

    def test_view_renders_the_same_template_as_render_template(self):
        """
        Ensures 'view' renders the same template that 'render_template'
        """
        # assert
        self.assertEqual(view('index'), render_template('index.html'))


if __name__ == '__main__':
    unittest.main()

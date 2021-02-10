import unittest

from unittest.mock import MagicMock

from account_verification_flask.models.models import User
from account_verification_flask.services.authy_services import AuthyServices

from .base import BaseTestCase


class AuthyTests(BaseTestCase):
    def test_unverified_user_with_valid_code_then_gets_verified(self):
        """
        Ensures unverified users get verified with the right verification
        """
        # arrange
        authy_service_mock = self._get_authy_right_code_validator()

        # act
        user = self._get_test_user()
        authy_service_mock.confirm_phone_number(user, "5464646464")

        # assert
        self.assertTrue(user.phone_number_confirmed)

    def test_unverified_user_with_invalid_code_then_gets_verified(self):
        """
        Ensures unverified users don't get verified with the right verification
        """
        # arrange
        authy_service_mock = self._get_authy_wrong_code_validator()

        # act
        user = self._get_test_user()
        authy_service_mock.confirm_phone_number(user, "5464646464")

        # assert
        self.assertFalse(user.phone_number_confirmed)

    def _get_authy_right_code_validator(self):
        authy_service_mock = AuthyServices()
        authy_service_mock.confirm_phone_number = MagicMock(
            return_value=True, side_effect=self._confirm_phone_number_right_side_effect
        )
        return authy_service_mock

    def _get_authy_wrong_code_validator(self):
        authy_service_mock = AuthyServices()
        authy_service_mock.confirm_phone_number = MagicMock(
            return_value=True, side_effect=self._confirm_phone_number_wrong_side_effect
        )
        return authy_service_mock

    @staticmethod
    def _confirm_phone_number_right_side_effect(user, code):
        user.phone_number_confirmed = True
        return True

    @staticmethod
    def _confirm_phone_number_wrong_side_effect(user, code):
        user.phone_number_confirmed = False
        return False

    @staticmethod
    def _get_test_user():
        return User(
            name="User",
            email="user@email.com",
            password="pass",
            country_code="1",
            phone_number="554885225",
        )


if __name__ == '__main__':
    unittest.main()

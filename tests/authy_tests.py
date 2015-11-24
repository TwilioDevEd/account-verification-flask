import unittest

from account_verification_flask.models.models import User
from account_verification_flask.services.authy_services import AuthyServices
from base import BaseTestCase
from mock import MagicMock


class AuthyTests(BaseTestCase):
    # Ensures unverified users get verified with the right verification
    def test_unverified_user_with_valid_code_then_gets_verified(self):
        # arrange
        authy_service_mock = self._get_authy_right_code_validator()

        # act
        user = self._get_test_user()
        authy_service_mock.confirm_phone_number(user, "5464646464")

        # assert
        assert user.phone_number_confirmed == True

    # Ensures unverified users don't get verified with the right verification
    def test_unverified_user_with_invalid_code_then_gets_verified(self):
        # arrange
        authy_service_mock = self._get_authy_wrong_code_validator()

        # act
        user = self._get_test_user()
        authy_service_mock.confirm_phone_number(user, "5464646464")

        # assert
        assert user.phone_number_confirmed == False

    def _get_authy_right_code_validator(self):
        authy_service_mock = AuthyServices()
        authy_service_mock.confirm_phone_number = MagicMock(return_value=True,
                                                            side_effect=self._confirm_phone_number_right_side_effect)
        return authy_service_mock

    def _get_authy_wrong_code_validator(self):
        authy_service_mock = AuthyServices()
        authy_service_mock.confirm_phone_number = MagicMock(return_value=True,
                                                            side_effect=self._confirm_phone_number_wrong_side_effect)
        return authy_service_mock

    def _confirm_phone_number_right_side_effect(self, user, code):
        user.phone_number_confirmed = True
        return True

    def _confirm_phone_number_wrong_side_effect(self, user, code):
        user.phone_number_confirmed = False
        return False

    def _get_test_user(self):
        return User(
            name="User",
            email="user@email.com",
            password="pass",
            country_code="1",
            phone_number="554885225"
        )


if __name__ == '__main__':
    unittest.main()

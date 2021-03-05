import account_verification_flask.utilities
from account_verification_flask.utilities.settings import AuthySettings
from authy.api import AuthyApiClient


class AuthyServices:
    authy_client = None

    def __init__(self):
        if AuthyServices.authy_client is None:
            AuthyServices.authy_client = AuthyApiClient(AuthySettings.key())

    def request_phone_confirmation_code(self, user):
        if user is None:
            raise ValueError(account_verification_flask.utilities.User_Id_Not_Found)

        if user.authy_user_id is None:
            self._register_user_under_authy(user)

        sms = self.authy_client.users.request_sms(user.authy_user_id, {'force': True})
        return not sms.ignored()

    def confirm_phone_number(self, user, verification_code):
        if user is None:
            raise ValueError(account_verification_flask.utilities.User_Id_Not_Found)

        verification = self.authy_client.tokens.verify(
            user.authy_user_id, verification_code
        )
        return verification.ok()

    def _register_user_under_authy(self, user):
        authy_user = self.authy_client.users.create(
            user.email, user.phone_number, user.country_code
        )
        if authy_user.ok:
            user.authy_user_id = authy_user.id

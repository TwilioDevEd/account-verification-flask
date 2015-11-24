from authy.api import AuthyApiClient
from account_verification_flask import app
from account_verification_flask.utilities.messages import ApplicationMessages
from account_verification_flask.utilities.settings import AuthySettings

class AuthyServices:
    authy_client = None

    def __init__(self):
        if AuthyServices.authy_client == None:
            AuthyServices.authy_client = AuthyApiClient(AuthySettings.key())

    def request_phone_confirmation_code(self, user):
        if user == None:
            raise ValueError(ApplicationMessages.User_Id_Not_Found)

        if user.authy_user_id == None:
            self._register_user_under_authy(user)

        sms = AuthyServices.authy_client.users.request_sms(user.authy_user_id, {'force': True})
        return not sms.ignored()

    def confirm_phone_number(self, user, verification_code):
        if user == None:
            raise ValueError(ApplicationMessages.User_Id_Not_Found)

        verification = AuthyServices.authy_client.tokens.verify(user.authy_user_id, verification_code)
        return verification.ok()

    def _register_user_under_authy(self, user):
        authy_user = AuthyServices.authy_client.users.create(user.email, user.phone_number, user.country_code)
        if authy_user.ok:
            user.authy_user_id = authy_user.id

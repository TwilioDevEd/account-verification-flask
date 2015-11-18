from authy.api import AuthyApiClient
from account_verification_flask import app

class AuthyServices:
    __authy_client = None

    def __init__(delf):
        if authy_client == None:
            authy_client = AuthyApiClient(app.config['AUTHY_KEY'] )

    def request_phone_confirmation_code(self, user):
        if user.authy_user_id == None:
            if _register_user_under_authy(user):
                sms = authy_client.users.request_sms(user.authy_user_id, {'force': True})
                return not sms.ignored()
        return False

    def _register_user_under_authy(self, user):
        authy_user = authy_client.users.create(user.email, user.phone_number, user.country_code)

        if authy_user.ok:
            user.authy_user_id = authy_user.id
            return True;
        
        return False;



import account_verification_flask.utilities
from account_verification_flask.utilities.settings import TwilioSettings
from twilio.rest import Client


class TwilioServices:
    twilio_client = None

    def __init__(self):
        if TwilioServices.twilio_client is None:
            TwilioServices.twilio_client = Client(
                TwilioSettings.api_key(),
                TwilioSettings.api_secret(),
                TwilioSettings.account_sid(),
            )

    def send_registration_success_sms(self, to_number):
        self.twilio_client.messages.create(
            body=account_verification_flask.utilities.Signup_Complete,
            to=to_number,
            from_=TwilioSettings.phone_number(),
        )

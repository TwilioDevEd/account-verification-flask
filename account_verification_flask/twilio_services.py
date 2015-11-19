from authy.api import AuthyApiClient
from account_verification_flask import app
from .messages import ApplicationMessages
from .settings import AuthySettings, TwilioSettings
from twilio.rest import TwilioRestClient

class TwilioServices:
    twilio_client = None

    def __init__(self):
        if TwilioServices.twilio_client == None:
            TwilioServices.twilio_client = TwilioRestClient(TwilioSettings.account_sid, TwilioSettings.auth_token)

    def send_registration_success_sms(self, to_number):
        message = TwilioServices.twilio_client.messages.create(body=ApplicationMessages.Signup_Complete,
            to=to_number,
            from_=TwilioSettings.phone_number) 


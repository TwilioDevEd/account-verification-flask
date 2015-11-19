from account_verification_flask import app

class AuthySettings:
    key = app.config['AUTHY_KEY']

class TwilioSettings:
    account_sid=app.config['TWILIO_ACCOUNT_SID']

    auth_token=app.config['TWILIO_AUTH_TOKEN']

    phone_number=app.config['TWILIO_NUMBER']

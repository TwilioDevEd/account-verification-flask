from account_verification_flask import app

class AuthySettings:
    @staticmethod
    def key():
        return app.config['AUTHY_KEY']

class TwilioSettings:
    @staticmethod
    def account_sid():
        return app.config['TWILIO_ACCOUNT_SID']
    
    @staticmethod
    def auth_token():
        return app.config['TWILIO_AUTH_TOKEN']

    @staticmethod
    def phone_number():
        return app.config['TWILIO_NUMBER']

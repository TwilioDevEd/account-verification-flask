from account_verification_flask import app


class AuthySettings:
    @staticmethod
    def key():
        return app.config['AUTHY_API_KEY']


class TwilioSettings:
    @staticmethod
    def account_sid():
        return app.config['TWILIO_ACCOUNT_SID']

    @staticmethod
    def api_key():
        return app.config['TWILIO_API_KEY']

    @staticmethod
    def api_secret():
        return app.config['TWILIO_API_SECRET']

    @staticmethod
    def phone_number():
        return app.config['TWILIO_NUMBER']

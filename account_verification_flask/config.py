﻿class DefaultConfig(object):
    SECRET_KEY = '%^!@@*!&$8xdfdirunb52438#(&^874@#^&*($@*(@&^@)(&*)Y_)((+'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class DevelopmentConfig(DefaultConfig):
    AUTHY_KEY = 'your_authy_key'

    TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
    TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
    TWILIO_NUMBER = 'your_twilio_phone_number'

    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    DEBUG = True

class TestConfig(DefaultConfig):
    SQLALCHEMY_ECHO = True

    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False

config_env_files = {
    'test': 'account_verification_flask.config.TestConfig',
    'development': 'account_verification_flask.config.DevelopmentConfig',
}

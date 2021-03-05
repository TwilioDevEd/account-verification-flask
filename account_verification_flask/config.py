import os

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
    TWILIO_API_KEY = os.environ.get('TWILIO_API_KEY', None)
    TWILIO_API_SECRET = os.environ.get('TWILIO_API_SECRET', None)
    TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', None)
    AUTHY_API_KEY = os.environ.get('AUTHY_API_KEY', None)

    DEBUG = False


class DevelopmentConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    DEBUG = True


class TestConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_ECHO = True
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


config_env_files = {
    'testing': 'account_verification_flask.config.TestConfig',
    'development': 'account_verification_flask.config.DevelopmentConfig',
    'production': 'account_verification_flask.config.Default',
}

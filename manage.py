"""
This script holds the commands nedeed for runnin the migrations and the tests
"""

from flask import Flask
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from account_verification_flask import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest, sys
    tests = unittest.TestLoader().discover('.', pattern="*_tests.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == "__main__":
    manager.run()

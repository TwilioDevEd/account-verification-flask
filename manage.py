"""
This script holds the commands nedeed for runnin the migrations and the tests
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from account_verification_flask import app, db, prepare_app

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import sys
    import unittest
    prepare_app(environment='testing')

    tests = unittest.TestLoader().discover('.', pattern="*_tests.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == "__main__":
    manager.run()

# Account Verification with Authy

![Flask](https://github.com/TwilioDevEd/account-verification-flask/workflows/Flask/badge.svg)

This application example demonstrates how to implement Account Verification
on a Python Flask application using [Authy](https://www.twilio.com/authy).

[Read the full tutorial here](https://www.twilio.com/docs/tutorials/walkthrough/account-verification/python/flask)!

## Quickstart

### Create an Authy app

Create a free [Authy application](https://www.twilio.com/console/authy/applications), if you don't
have one already.

### Local development

This project is built using the [Flask](http://flask.pocoo.org/) web framework.
For now, it only runs on Python 2.7 (not 3.4+).

1. To run the app locally, clone this repository and `cd` into it.

1. Create and activate a new python3 virtual environment.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

1. Install the requirements.

    ```bash
    pip install -r requirements.txt
    ```

1. Copy the sample configuration file and edit it to match your configuration.

   ```bash
   cp .env.example .env
   ```

   Twilio API credentials can be found [here](https://www.twilio.com/console) 
   and find you can create a REST API Key [here](https://www.twilio.com/console/project/api-keys).
   If using the twilio CLI you can run:
   
   ```bash
   twilio api:core:keys:create --friendly-name=worm-transfer -o json
   ```
   
   Copy or create a Twilio phone number from [here](https://www.twilio.com/console/phone-numbers).

1. Run the migrations.

    ```bash
    python manage.py db upgrade
    ```

1. Start the development server.

    ```bash
    python manage.py runserver
    ```

1. Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

That's it!

## Run the tests locally.

   ```bash
   python manage.py test
   ```

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](LICENSE)
* Lovingly crafted by Twilio Developer Education.

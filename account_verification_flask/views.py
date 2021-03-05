from flask import request, flash, g
from flask_login import login_user, logout_user, current_user
from account_verification_flask import app, db, login_manager
from account_verification_flask.forms.forms import (
    RegisterForm,
    ResendCodeForm,
    VerifyCodeForm,
)
from account_verification_flask.models.models import User
from account_verification_flask.services.authy_services import AuthyServices
from account_verification_flask.services.twilio_services import TwilioServices
from account_verification_flask.utilities import User_Already_Confirmed
from account_verification_flask.utilities.view_helpers import view, redirect_to
import account_verification_flask.utilities


@app.route('/')
@app.route('/home')
def home():
    return view('index')


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():

            if User.query.filter(User.email == form.email.data).count() > 0:
                form.email.errors.append(
                    account_verification_flask.utilities.User_Email_Already_In_Use
                )
                return view('register', form)

            user = User(
                name=form.name.data,
                email=form.email.data,
                password=form.password.data,
                country_code=form.country_code.data,
                phone_number=form.phone_number.data,
            )
            db.session.add(user)
            db.session.commit()

            authy_services = AuthyServices()
            if authy_services.request_phone_confirmation_code(user):
                db.session.commit()
                flash(account_verification_flask.utilities.Verification_Code_Sent)
                return redirect_to('verify', email=form.email.data)

            form.email.errors.append(
                account_verification_flask.utilities.Verification_Code_Not_Sent
            )

        else:
            return view('register', form)

    return view('register', form)


@app.route('/verify', methods=["GET", "POST"])
@app.route('/verify/<email>', methods=["GET"])
def verify():
    form = VerifyCodeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter(User.email == form.email.data).first()

            if user is None:
                form.email.errors.append(
                    account_verification_flask.utilities.User_Not_Found_For_Given_Email
                )
                return view('verify_registration_code', form)

            if user.phone_number_confirmed:
                form.email.errors.append(User_Already_Confirmed)
                return view('verify_registration_code', form)

            authy_services = AuthyServices()
            if authy_services.confirm_phone_number(user, form.verification_code.data):
                user.phone_number_confirmed = True
                db.session.commit()
                login_user(user, remember=True)
                twilio_services = TwilioServices()
                twilio_services.send_registration_success_sms(
                    "+{0}{1}".format(user.country_code, user.phone_number)
                )
                return redirect_to('status')
            else:
                form.email.errors.append(
                    account_verification_flask.utilities.Verification_Unsuccessful
                )
                return view('verify_registration_code', form)
    else:
        form.email.data = request.args.get('email')
    return view('verify_registration_code', form)


@app.route('/resend', methods=["GET", "POST"])
@app.route('/resend/<email>', methods=["GET"])
def resend(email=""):
    form = ResendCodeForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter(User.email == form.email.data).first()

            if user is None:
                form.email.errors.append(
                    account_verification_flask.utilities.User_Not_Found_For_Given_Email
                )
                return view('resend_confirmation_code', form)

            if user.phone_number_confirmed:
                form.email.errors.append(
                    account_verification_flask.utilities.User_Already_Confirmed
                )
                return view('resend_confirmation_code', form)
            authy_services = AuthyServices()
            if authy_services.request_phone_confirmation_code(user):
                flash(account_verification_flask.utilities.Verification_Code_Resent)
                return redirect_to('verify', email=form.email.data)
            else:
                form.email.errors.append(
                    account_verification_flask.utilities.Verification_Code_Not_Sent
                )
    else:
        form.email.data = email

    return view('resend_confirmation_code', form)


@app.route('/status')
def status():
    return view('status')


@app.route('/logout', methods=["POST"])
def logout():
    logout_user()
    return redirect_to('home')


# controller utils
@app.before_request
def before_request():
    g.user = current_user


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except Exception:
        return None

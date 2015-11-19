from datetime import datetime
from flask import session, request, flash, url_for, abort ,g
from flask.ext.login import login_user , logout_user, current_user, login_required
 

from account_verification_flask import app, db, login_manager
from .forms import RegisterForm, VerifyCodeForm, ResendCodeForm
from .models import User
from .messages import ApplicationMessages
from .authy_services import AuthyServices
from .twilio_services import TwilioServices
from .controller_helpers import redirect_to, view


@app.route('/')
@app.route('/home')
def home():
    return view('index')  


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():

            if User.query.filter(User.email == form.email.data).count()>0 :
                form.email.errors.append(ApplicationMessages.User_Email_Already_In_Use)
                return view('register', form)

            user = User(
                name=form.name.data,
                email=form.email.data,
                password=form.password.data,
                country_code=form.country_code.data,
                phone_number=form.phone_number.data
            )
            db.session.add(user)
            db.session.commit()

            if AuthyServices().request_phone_confirmation_code(user):
                db.session.commit()
                flash(ApplicationMessages.Verification_Code_Sent)
                return redirect_to('verify', email=form.email.data)

            form.email.errors.append(ApplicationMessages.Verification_Code_Not_Sent)

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

            if user == None:
                form.email.errors.append(ApplicationMessages.User_Not_Found_For_Given_Email)
                return view('verify_registration_code', form)

            if user.phone_number_confirmed:
                form.email.errors.append(ApplicationMessages.User_Already_Confirmed)
                return view('verify_registration_code', form)

            if AuthyServices().confirm_phone_number(user, form.verification_code.data):
                user.phone_number_confirmed = True
                db.session.commit()
                login_user(user, remember=True)
                TwilioServices().send_registration_success_sms("+{0}{1}".format(user.country_code, user.phone_number))
                return redirect_to('status')
            else:
                form.email.errors.append(ApplicationMessages.Verification_Unsuccessful)
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

            if user == None:
                form.email.errors.append(ApplicationMessages.User_Not_Found_For_Given_Email)
                return view('resend_confirmation_code', form)

            if user.phone_number_confirmed:
                form.email.errors.append(ApplicationMessages.User_Already_Confirmed)
                return view('resend_confirmation_code', form )

            if AuthyServices().request_phone_confirmation_code(user):
                flash(ApplicationMessages.Verification_Code_Resent)
                return redirect_to('verify', email=form.email.data)
            else:
                form.email.errors.append(ApplicationMessages.Verification_Code_Not_Sent)
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


# utilities

@app.before_request
def before_request():
    u = User.query.get(22)
    g.user = current_user

@login_manager.user_loader
def load_user (id):
    try:
        return User.query.get(id)
    except:
        return None
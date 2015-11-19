from datetime import datetime
from flask import session, request, flash, url_for, redirect, render_template, abort ,g
from flask.ext.login import login_user , logout_user, current_user, login_required
 

from account_verification_flask import app, db, login_manager
from .forms import RegisterForm, VerifyRegistrationCodeForm, ResendCodeForm
from .models import User
from .messages import ApplicationMessages
from .authy_services import AuthyServices
from .utilities import Struct

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')  


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():

            if User.query.filter(User.email == form.email.data).count()>0 :
                form.email.errors.append(ApplicationMessages.User_Email_Already_In_Use)
                return render_template('register.html', form = form)

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
                return redirect(url_for('verify', email=form.email.data))

            form.email.errors.append(ApplicationMessages.Verification_Code_Not_Sent)

        else: 
            return render_template('register.html', form = form)

    return render_template('register.html', form = form)  

@app.route('/verify', methods=["GET", "POST"])
@app.route('/verify/<email>', methods=["GET"])
def verify():
    form = VerifyRegistrationCodeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter(User.email == form.email.data).first()

            if user == None:
                form.email.errors.append(ApplicationMessages.User_Not_Found_For_Given_Email)
                return render_template('verify_registration_code.html', form = form)

            if user.phone_number_confirmed:
                form.email.errors.append(ApplicationMessages.User_Already_Confirmed)
                return render_template('verify_registration_code.html', form = form)

            if AuthyServices().confirm_phone_number(user, form.verification_code.data):
                user.phone_number_confirmed = True
                db.session.commit()
                login_user(user, remember=True)
                # send sms
                return redirect(url_for('status'))
            else:
                form.email.errors.append(ApplicationMessages.Verification_Unsuccessful)
                return render_template('verify_registration_code.html', form = form)
    else:
        form.email.data = request.args.get('email')
    return render_template('verify_registration_code.html', form = form)  


@app.route('/resend', methods=["GET", "POST"])
@app.route('/resend/<email>', methods=["GET"])
def resend(email=""):
    form = ResendCodeForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter(User.email == form.email.data).first()

            if user == None:
                form.email.errors.append(ApplicationMessages.User_Not_Found_For_Given_Email)
                return render_template('resend_confirmation_code.html', form = form)

            if user.phone_number_confirmed:
                form.email.errors.append(ApplicationMessages.User_Already_Confirmed)
                return render_template('resend_confirmation_code.html', form = form)

            if AuthyServices().request_phone_confirmation_code(user):
                flash(ApplicationMessages.Verification_Code_Resent)
                return redirect(url_for('verify', email=form.email.data))
            else:
                form.email.errors.append(ApplicationMessages.Verification_Code_Not_Sent)
    else:
        form.email.data = email

    return render_template('resend_confirmation_code.html', form = form) 

@app.route('/status')
def status():
    return render_template('status.html')  


@app.route('/logout', methods=["POST"])
def logout():
    logout_user()
    return redirect(url_for('home')) 


# utilities

@app.errorhandler(500)
def internal_error(error):
    return error

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
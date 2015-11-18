from datetime import datetime
from flask import session, request, flash, url_for, redirect, render_template, abort ,g
from flask.ext.login import login_user , logout_user, current_user, login_required

from account_verification_flask import app, db, login_manager
from .forms import RegisterForm
from .models import User
from .messages import ApplicationMessages
from .authy_services import AuthyServices

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
                form.password.errors.append(ApplicationMessages.User_Email_Already_In_Use)
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
            login_user(user, remember=True)
            return redirect(url_for('home'))

            #authy_services = AuthyServices()
            #if authy_services.request_phone_confirmation_code(user):
            #    db.session.commit()
            #    return redirect(url_for('verify'))

            #form.email.errors.append(ApplicationMessages.Verification_Code_Not_Sent)

        else: 
            return render_template('register.html', form = form)

    return render_template('register.html', form = form)  


@app.route('/verify')
def verifiy_registration_code():
    return render_template('verify_registratrion_code.html')  

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
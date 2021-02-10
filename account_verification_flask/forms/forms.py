from flask_wtf import FlaskForm
from wtforms import PasswordField, IntegerField, StringField
from wtforms.validators import DataRequired, Length, Email


class RegisterForm(FlaskForm):
    name = StringField(
        'Tell us your name',
        validators=[
            DataRequired(message="Name is required"),
            Length(min=3, message="Name must greater than 3 chars"),
        ],
    )
    email = StringField(
        'Enter your E-mail',
        validators=[
            DataRequired("E-mail is required"),
            Email(message="Invalid E-mail address"),
        ],
    )
    password = PasswordField(
        'Password', validators=[DataRequired("Password is required")]
    )
    country_code = StringField(
        'Country Code',
        validators=[
            DataRequired("Country code is required"),
            Length(min=1, max=4, message="Country must be between 1 and 4 chars"),
        ],
    )

    phone_number = IntegerField(
        'Phone Number', validators=[DataRequired("Valid phone number is required")]
    )


class ResendCodeForm(FlaskForm):
    email = StringField(
        'E-mail',
        validators=[
            DataRequired("E-mail is required"),
            Email(message="Invalid E-mail address"),
        ],
    )


class VerifyCodeForm(ResendCodeForm):
    verification_code = StringField(
        'Verification Code', validators=[DataRequired("Verification code is required")]
    )

from flask import url_for
from wtforms import (
    StringField, PasswordField, SubmitField, BooleanField, 
    HiddenField)

from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp, Optional

# import email_validator
from wtforms import ValidationError
from app.auth.register_service import check_pwd_credential, email_already_registered, username_already_registered

from app.models.moviegoer import Moviegoer
from app.models.principal import Principal
from ..models import PasswordCredential


class login_form(FlaskForm):
    # email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    username = StringField(
        label="Username",
        render_kw={"placeholder": "Your Username"},
        validators=[InputRequired()])
    password = PasswordField(
        label="Password",
        render_kw={"placeholder": "Password"},
        validators=[InputRequired(), Length(min=8, max=72)])
    remember_me = BooleanField(
        label="Remember Me",
        render_kw={"placeholder": "Remember Me"},
        validators=[Optional()])
    principal = HiddenField("principal")
    
    # Placeholder labels to enable form rendering
    submit_button = SubmitField("Login",
        render_kw={"class": "btn-lg"})

    def validate_principal(self, *args, **kwargs):
        un = self.username.data
        pw = self.password.data
        principal, err = check_pwd_credential(un, pw)
        if err:
            self.principal.data = None
            raise ValidationError(err)
        else:
            self.principal.data = principal

class register_form(FlaskForm):
    username = StringField(
        label="Username",
        validators=[
            InputRequired(),
            Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, " "numbers, dots or underscores",
            ),
        ]
    )
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    password = PasswordField(validators=[InputRequired(), Length(8, 72)])
    confirmPassword = PasswordField(
        validators=[
            InputRequired(),
            Length(8, 72),
            EqualTo("password", message="Passwords must match !"),
        ]
    )
    submit_button = SubmitField("Submit This Form")

    def validate_email(self, email):
        if email_already_registered(email.data):
            raise ValidationError("Email already registered!")

    def validate_username(self, username):
        if username_already_registered(username.data):
            raise ValidationError("Username already taken!")

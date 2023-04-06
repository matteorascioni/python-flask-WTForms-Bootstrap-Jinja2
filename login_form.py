from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, validators

class LoginForm(FlaskForm):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8)])
    submit = SubmitField('Submit')
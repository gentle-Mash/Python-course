from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo, Email


class Registration(FlaskForm):
    username = StringField(label="User Name:", validators=[Length(min=3, max=30), DataRequired()])
    email = StringField(label="Email Address:", validators=[DataRequired(), Email()])
    password1 = PasswordField(label="Create an strong password:", validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField(label="Confirm your password:", validators=[DataRequired(), EqualTo('password1') ])
    submit = SubmitField(label="Create your account")
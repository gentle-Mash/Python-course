from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo


class Registration(FlaskForm):
    username = StringField(label="User Name:", validators=[Length(min=4, max=30), DataRequired()])
    email = StringField(label="Email Address:", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Create an strong password:", validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label="Confirm your password:", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Create your account")
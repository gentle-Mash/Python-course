from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    book = StringField('Book name', validators=[DataRequired()])
    author = StringField('Author name', validators=[DataRequired()])
    book_rating = FloatField("Book Rating", validators=[DataRequired()])
    submit = SubmitField('Submit')

class Edit(FlaskForm):
    change_rating = FloatField("Update Book Rating", validators=[DataRequired()])
    submit = SubmitField('Submit')
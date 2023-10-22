from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Edit(FlaskForm):
    update_rating = StringField("Update Movie Rating", validators=[DataRequired()])
    update_review = StringField("Update Your review", validators=[DataRequired()])
    submit = SubmitField('Done')

class Add(FlaskForm):
        movie_title = StringField("Movie Title", validators=[DataRequired()])
        submit = SubmitField('Done')


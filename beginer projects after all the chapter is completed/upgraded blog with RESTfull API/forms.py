from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

class NewPost(FlaskForm):
    title = StringField(label="Your Blog title", validators=[DataRequired()])
    subtitle = StringField(label="Give a subtitle of your blog", validators=[DataRequired()])
    author = StringField(label="Author's Name", validators=[DataRequired()])
    img_url = StringField(label="Give an image url about your blog", validators=[URL()])
    body = CKEditorField(label="Content", validators=[DataRequired()])
    submit = SubmitField(label="Post")



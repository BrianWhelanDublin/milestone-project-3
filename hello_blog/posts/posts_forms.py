from flask_wtf import FlaskForm
from wtforms import (SelectField, StringField,
                     SubmitField, TextAreaField)
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    category = SelectField("Category", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Post Content", validators=[DataRequired()])
    submit = SubmitField("Add Post")

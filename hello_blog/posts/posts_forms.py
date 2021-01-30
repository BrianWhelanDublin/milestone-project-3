from flask_wtf import FlaskForm
from wtforms import (SelectField, StringField,
                     SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    category = SelectField("Category", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired(),
                        Length(min=5, max=50)])
    content = TextAreaField("Post Content", validators=[DataRequired()])
    submit = SubmitField("Post")


class DeletePostForm(FlaskForm):
    submit = SubmitField("Delete")


class CommentForm(FlaskForm):
    comment = StringField("Add Comment", validators=[DataRequired()])
    submit = SubmitField("Comment")

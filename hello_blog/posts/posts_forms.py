from flask_wtf import FlaskForm
from wtforms import (SelectField, StringField,
                     SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Length


# Post form to add new post
class PostForm(FlaskForm):
    category = SelectField("Category")
    title = StringField("Title", validators=[DataRequired(),
                                             Length(min=2, max=50)])
    content = TextAreaField("Post Content", validators=[DataRequired()])
    submit = SubmitField("Post")


# Form to delete a post
class DeletePostForm(FlaskForm):
    delete = SubmitField("Delete")


# Form to add a comment
class CommentForm(FlaskForm):
    comment = StringField("Add Comment", validators=[DataRequired()])
    submit = SubmitField("Comment")


#  Form to update a comment
class UpdateCommentForm(FlaskForm):
    comment = StringField("Update Comment", validators=[DataRequired()])
    submit = SubmitField("Update")


#  Form to earch the posts by text.
class SearchForm(FlaskForm):
    search = StringField("Search Posts", validators=[DataRequired(),
                                                     Length(min=3)])
    submit = SubmitField("Search")

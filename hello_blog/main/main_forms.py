from flask_wtf import FlaskForm
from wtforms import (StringField,
                     SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Length, Email


# Contact us form
class ContactForm(FlaskForm):
    name = StringField("Name",
                       validators=[DataRequired(),
                                   Length(min=3, max=20)])
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Contact us")

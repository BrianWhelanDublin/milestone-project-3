from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (StringField, PasswordField,
                     SubmitField, BooleanField, TextAreaField)
from wtforms.validators import (DataRequired, Length, Email,
                                EqualTo, ValidationError)
from hello_blog.models import User
from flask_login import current_user


# creates the form and validaters for the user to sign up.
class SignupForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(),
                                       Length(min=3, max=20)])
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                             validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(),
                                                 EqualTo("password")])
    submit = SubmitField("Sign Up")

    # create functions to check if username and email aready exist
    #  using flask wtforms custom validators
    # in the database and if they do it will throw a validation error
    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username already signedup.")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError("Email already signedup.")


#  create form for login route
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_user = BooleanField("Remember Me")
    submit = SubmitField("Login")


# create form for updating account
class UpdateAccount(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(),
                                       Length(min=3, max=20)])
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    bio = TextAreaField("Bio", [Length(min=10, max=150)],
                        render_kw={"data-length": "150"})
    user_image = FileField("Update Profile Image",
                           validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField("Update")

    # use custom validators to insure the username and email is unique
    # only run if the user has changed the data
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.objects(username=username.data).first()
            if user is not None:
                raise ValidationError("Username already in use.\
                    Please try another")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.objects(email=email.data).first()
            if user is not None:
                raise ValidationError("Email already in use.\
                    Please try another")


class DeleteAccountForm(FlaskForm):
    submit = SubmitField("Delete")

from flask import Blueprint, render_template, url_for, flash, redirect
from hello_blog.users.forms import SignupForm
from hello_blog.models import User


users = Blueprint("users", __name__)


# create the users route where users can sign up
@users.route("/signup", methods=["GET", "POST"])
def signup():
    # use form created in users.forms.py
    form = SignupForm()
    # checks if the form is valid using wtf validators
    if form.validate_on_submit():
        # creates an instance of User class from form data
        # and then hashes thier password
        # and saves this user to the database in mongodb
        user = User(username=form.username.data,
                    email=form.email.data)
        user.hash_password(form.password.data)
        user.save()
        flash("User registered", "success")
        return redirect(url_for("main.home"))
    return render_template("users/signup.html",
                           title="Sign Up",
                           form=form)

from flask import Blueprint, render_template, url_for, flash, redirect
from hello_blog.users.forms import SignupForm


users = Blueprint("users", __name__)


# create the users route where users can sign up
@users.route("/signup", methods=["GET", "POST"])
def signup():
    # use form created in users.forms.py
    form = SignupForm()
    # checks if the form is valid using wtf validators
    if form.validate_on_submit():
        flash("User registered", "success")
        return redirect(url_for("users.signup"))
    return render_template("users/signup.html",
                           title="Sign Up",
                           form=form)

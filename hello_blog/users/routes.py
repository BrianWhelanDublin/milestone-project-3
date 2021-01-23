from flask import Blueprint, render_template
from hello_blog.users.forms import SignupForm


users = Blueprint("users", __name__)


# create the users route where users can sign up
@users.route("/signup")
def signup():
    # use form created in users.forms.py
    form = SignupForm()
    return render_template("users/signup.html",
                           title="Sign Up",
                           form=form)

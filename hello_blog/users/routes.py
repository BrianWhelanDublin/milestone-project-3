from flask import Blueprint, render_template
from hello_blog.users.forms import SignupForm


users = Blueprint("users", __name__)


@users.route("/signup")
def signup():
    form = SignupForm()
    return render_template("users/signup.html",
                           title="Sign Up",
                           form=form)
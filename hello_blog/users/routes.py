from flask import (Blueprint, render_template, url_for,
                   flash, redirect)
from hello_blog.users.forms import SignupForm, LoginForm, UpdateAccount
from hello_blog.models import User
from hello_blog import bcrypt
from flask_login import login_user, current_user, logout_user, login_required


users = Blueprint("users", __name__)


# create the users route where users can sign up
@users.route("/signup", methods=["GET", "POST"])
def signup():
    # if the user has logged in and gets to
    # this route they will be redirected home
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
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
        flash("User registered, Please login now", "success")
        return redirect(url_for("users.login"))
    return render_template("users/signup.html",
                           title="Sign Up",
                           form=form)


#  create the route to login the user.
@users.route("/login", methods=["GET", "POST"])
def login():
    # if the user has logged in and gets to
    # this route they will be redirected home
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        # Finds the user in the database by their username
        user = User.objects(
            username=form.username.data).first()

        # if user exists use bycrpt check passsword hashes
        # function to check the passwords match
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember_user.data)
            flash("You've been logged in successfully", "success")
            return redirect(url_for("main.home"))

        # if no user exists or wrong details lets
        # user know and directs them back to the login page
        else:
            flash("Login Unsuccessful. Please check login details", "errors")
            return redirect(url_for("users.login"))
    return render_template("users/login.html",
                           title="Login",
                           form=form)


#  create the route to logout the user.
@users.route("/logout")
def logout():
    logout_user()
    flash("You've been logged out succesfully", "success")
    return redirect(url_for("main.home"))


@users.route("/account/<username>")
@login_required
def account(username):
    user = User.objects(username=username).first_or_404()
    return render_template("users/account.html",
                           user=user)


# create the route for updating the users account
@users.route("/update/account", methods=["GET", "POST"])
@login_required
def update_account():
    form = UpdateAccount()
    if form.validate_on_submit():
        return redirect(url_for("users.account",
                                username=current_user.username))
    return render_template("users/update_account.html",
                           form=form)

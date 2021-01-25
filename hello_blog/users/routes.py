from flask import (Blueprint, render_template, url_for,
                   flash, redirect, request)
from hello_blog.users.forms import SignupForm, LoginForm, UpdateAccount
from hello_blog.models import User
from hello_blog import bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from hello_blog.users.utils import save_user_image


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
    # checks the form and changes the data in the database
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        # if the user adds an image it calls the save user image
        # function from utils to upload image to cloudinary
        if form.user_image.data:
            image_url = save_user_image(form.user_image.data)
            current_user.user_image = image_url
        if form.bio.data:
            current_user.bio = form.bio.data
        current_user.save()
        return redirect(url_for("users.account",
                                username=current_user.username))

    #  fills the form with the current data from the database
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
        if current_user.bio:
            form.bio.data = current_user.bio
    return render_template("users/update_account.html",
                           title="account",
                           form=form)


# create route to delete user
@users.route("/delete/account")
@login_required
def delete_account():
    # find user in database and delete their details
    user = User.objects(username=current_user.username).first()
    user.delete()
    flash("Account deleted successfully", "success")
    return redirect(url_for("main.home"))

from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

main = Blueprint("main", __name__)


# renders the main home page
@main.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("posts.all_posts"))
    return render_template("main/home.html")


# renders the about page
@main.route("/about")
def about():
    return render_template("main/about.html",
                           title="About Page")

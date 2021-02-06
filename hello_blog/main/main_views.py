from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
from hello_blog.models import Post
from hello_blog.main.main_forms import ContactForm


# Creates the main blueprint
main = Blueprint("main", __name__)


# renders the main home page displaying recent posts
@main.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("posts.all_posts"))
    posts = Post.objects().order_by("-date_posted")
    return render_template("main/home.html",
                           posts=posts)


# renders the about page
@main.route("/about")
def about():
    return render_template("main/about.html",
                           title="About Page")


# create the contact us route
@main.route("/contact")
def contact():
    form = ContactForm()
    return render_template("main/contact.html",
                           form=form,
                           title="Contact Us")

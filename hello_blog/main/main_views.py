from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user
from hello_blog.models import Post
from hello_blog.main.main_forms import ContactForm
from hello_blog import mail
from flask_mail import Message


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
@main.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "GET":
        # prefills users email if they are logged in
        if current_user.is_authenticated:
            form.email.data = current_user.email
    if form.validate_on_submit():
        msg = Message("Contact",
                      sender=form.name.data,
                      recipients=["briandublin1984@gmail.com"])
        msg.body = f''' {form.name.data} Is contacting you,
There message is: {form.message.data},
They can be contacted at {form.email.data}
'''
        mail.send(msg)
        flash("Contact message has been send", "success")
        return redirect(url_for("main.home"))
    return render_template("main/contact.html",
                           form=form,
                           title="Contact Us")

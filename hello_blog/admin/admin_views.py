from flask import Blueprint, render_template, abort, url_for
from flask_login import login_required, current_user
from hello_blog.models import User, Post, Categories

admin = Blueprint("admin", __name__)


@admin.route("/dashboard")
@login_required
def dashboard():
    if current_user.username != "admin":
        abort(403)
    users = User.objects()
    posts = Post.objects()
    categories = Categories.objects()
    return render_template("admin/dashboard.html",
                           title="Dashboard",
                           users=users,
                           posts=posts,
                           categories=categories)


@admin.route("/add/category")
@login_required
def add_category():
    if current_user.username != "admin":
        abort(403)
    return render_template("admin/add_category.html", title="Add Category")

from flask import Blueprint, render_template, abort, redirect, url_for, flash
from flask_login import login_required, current_user
from hello_blog.models import User, Post, Categories
from hello_blog.admin.admin_forms import AddCategoryForm
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


@admin.route("/add/category", methods=["GET", "POST"])
@login_required
def add_category():
    if current_user.username != "admin":
        abort(403)
    form = AddCategoryForm()
    if form.validate_on_submit():
        category = Categories(
            category_name=form.category_name.data
        )
        category.save()
        flash("Category saved", "success")
        return redirect(url_for('admin.dashboard'))
    return render_template("admin/add_category.html",
                           title="Add Category",
                           form=form)

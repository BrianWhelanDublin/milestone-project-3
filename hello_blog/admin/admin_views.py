from flask import (Blueprint, render_template,
                   abort, redirect, url_for,
                   flash, request)
from flask_login import login_required, current_user
from hello_blog.models import User, Post, Categories
from hello_blog.admin.admin_forms import (AddCategoryForm,
                                          EditCategoryForm,
                                          DeleteCategoryForm)


admin = Blueprint("admin", __name__)


# Displays the admin dashboard and the
#  amount of users and posts. Also desplays the current categories.
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
                           categories=categories,)


# Display the add category route and adds a category
# on a valid form submition.
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


# Displays the edit category route and also prefils the form with current data
# and updates the data on valid form submit.
@admin.route("/edit/category/<category_id>", methods=["GET", "POST"])
@login_required
def edit_category(category_id):
    if current_user.username != "admin":
        abort(403)
    category = Categories.objects().get_or_404(id=category_id)
    form = EditCategoryForm()
    if request.method == "GET":
        form.category_name.data = category.category_name
    if form.validate_on_submit():
        category.category_name = form.category_name.data
        category.save()
        flash("Category has been changed", "success")
        return redirect(url_for('admin.dashboard'))
    return render_template("admin/edit_category.html",
                           form=form,
                           title="Edit Category")


#  Deletes the current category and all posts within this category.
@admin.route("/delete/category/<category_id>", methods=["GET", "POST"])
@login_required
def delete_category(category_id):
    if current_user.username != "admin":
        abort(403)
    form = DeleteCategoryForm()
    if request.method == "POST":
        category = Categories.objects().get_or_404(id=category_id)
        posts = Post.objects(category=category)
        category.delete()
        posts.delete()
        flash("Category has been deleted", "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/delete_category.html",
                           title="Delete Category",
                           form=form)

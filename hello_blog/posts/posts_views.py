from flask import Blueprint, render_template
from flask_login import login_required
from hello_blog.models import Categories, Post
from hello_blog.posts.posts_forms import PostForm


posts = Blueprint("posts", __name__)


# create the route for the main post page to show
#  all recent posts to the user
@posts.route("/posts")
@login_required
def all_posts():
    return render_template("posts/all_posts.html",
                           title="All Posts")


# create the route to add new post
@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def add_post():
    form = PostForm()
    # get categories and loop thorough them
    categories = [(
        cat.category_name) for cat in Categories.objects]
    form.category.choices = categories
    return render_template("posts/new_post.html",
                           titile="New Post",
                           form=form)

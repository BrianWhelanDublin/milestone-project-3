from flask import Blueprint, render_template
from flask_login import login_required


posts = Blueprint("posts", __name__)


# create the route for the main post page to show
#  all recent posts to the user
@posts.route("/posts")
@login_required
def all_posts():
    return render_template("posts/all_posts.html",
                           title="Recent Posts")

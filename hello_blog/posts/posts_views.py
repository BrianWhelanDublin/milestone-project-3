from flask import (Blueprint, render_template, redirect,
                   url_for, flash, abort, request)
from flask_login import login_required, current_user
from hello_blog.models import Categories, Post, Comment
from hello_blog.posts.posts_forms import (PostForm, DeletePostForm, CommentForm,
                                          UpdateCommentForm, DeleteCommentForm)


posts = Blueprint("posts", __name__)


# create the route for the main post page to show
#  all recent posts to the user
@posts.route("/posts")
@login_required
def all_posts():
    page = request.args.get("page", 1, type=int)
    posts = Post.objects().order_by("-date_posted").paginate(
        page=page, per_page=4
    )
    return render_template("posts/all_posts.html",
                           title="All Posts",
                           posts=posts)


# create the route to add new post
@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def add_post():
    form = PostForm()
    # get categories and loop thorough them
    categories = [(
        cat.category_name) for cat in Categories.objects]
    form.category.choices = categories

    # add the post to the database on form submit
    if form.validate_on_submit():
        category = Categories.objects(
            category_name=form.category.data).first()
        post = Post(title=form.title.data,
                    content=form.content.data,
                    author=current_user.id,
                    category=category.id)
        post.save()
        flash("post has been posted successfully", "success")
        return redirect(url_for("posts.all_posts"))
    return render_template("posts/new_post.html",
                           titile="New Post",
                           form=form)


# create the route for the post page.
@posts.route("/post/<post_id>", methods=["POST", "GET"])
@login_required
def post(post_id):
    delete_form = DeletePostForm()
    comment_form = CommentForm()
    post = Post.objects().get_or_404(id=post_id)
    comments = Comment.objects(post=post)
    if request.method == "POST":
        comment = Comment(
            comment=comment_form.comment.data,
            comment_author=current_user.id,
            post=post
        )
        comment.save()
        flash("Comment added", "success")
        return redirect(url_for("posts.post", post_id=post.id))

    return render_template("posts/post.html",
                           title=post.title,
                           post=post,
                           delete_form=delete_form,
                           comments=comments,
                           comment_form=comment_form)


# create the update post route
@posts.route("/post/<post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = Post.objects().get_or_404(id=post_id)

    # throw a 403 error if a user has managed to get to this
    #  page and they weren't the posts author.
    if post.author.id != current_user.id:
        abort(403)
    form = PostForm()
    categories = [(
        cat.category_name) for cat in Categories.objects]
    form.category.choices = categories

    if form.validate_on_submit():
        category = Categories.objects(
            category_name=form.category.data).first()
        post.title = form.title.data
        post.content = form.content.data
        post.category = category.id
        post.save()
        flash("Your post has been updated", "success")
        return redirect(url_for("posts.post", post_id=post.id))

    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content

    return render_template("posts/update_post.html",
                           title="Update Post",
                           form=form)


#  create the delete post route similar to the delete user route.
@posts.route("/post/<post_id>/delete", methods=["GET", "POST"])
@login_required
def delete_post(post_id):
    if request.method == "POST":
        post = Post.objects.get_or_404(id=post_id)
        post.delete()
        flash("Post deleted successfully", "success")
        return redirect(url_for("main.home"))
    return abort(404)


#  create the route to update comment
@posts.route("/post/<post_id>/<comment_id>/update/comment",
             methods=["POST", "GET"])
@login_required
def update_comment(post_id, comment_id):
    delete_form = DeletePostForm()
    comment_form = UpdateCommentForm()
    post = Post.objects().get_or_404(id=post_id)
    comments = Comment.objects(post=post)
    comment = Comment.objects.get_or_404(id=comment_id)

    if request.method == "GET":
        comment_form.comment.data = comment.comment
        print(request.endpoint)

    if comment_form.validate_on_submit():
        comment.comment = comment_form.comment.data
        comment.save()
        flash("Comment has been updated", "success")
        return redirect(url_for("posts.post", post_id=post_id))

    return render_template("posts/post.html",
                           title="Update Comment",
                           post=post,
                           delete_form=delete_form,
                           comments=comments,
                           comment_form=comment_form)


@posts.route("/post/<post_id>/<comment_id>/delete", methods=["GET", "POST"])
@login_required
def delete_comment(post_id, comment_id):
    comment = Comment.objects.get_or_404(id=comment_id)
    if comment.comment_author.id != current_user.id:
        abort(404)
    else:
        comment.delete()
        flash("Comment deleted successfully", "success")
        return redirect(url_for("posts.post", post_id=post_id))

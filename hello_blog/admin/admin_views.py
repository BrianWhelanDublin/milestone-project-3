from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user

admin = Blueprint("admin", __name__)


@admin.route("/dashboard")
@login_required
def dashboard():
    if current_user.username != "admin":
        abort(403)
    return render_template("admin/dashboard.html")

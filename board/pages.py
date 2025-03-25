from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("/pages/about.html")

@bp.route("/contact_us")
def contact_us():
    return render_template("/pages/contact_us.html")
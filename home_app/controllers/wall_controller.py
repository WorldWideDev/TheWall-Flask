from home_app import app
from flask import render_template, redirect, request, session
from home_app.controllers.home_controller import LOGIN_KEY
from home_app.models import user as user_model, post as post_model


@app.route("/wall")
def wall():
    if not LOGIN_KEY in session:
        return redirect("/")
    return render_template("wall.html", posts=post_model.Post.get_all())

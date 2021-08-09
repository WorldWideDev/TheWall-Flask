from home_app import app
from flask import render_template, redirect, request, session
from home_app.controllers.home_controller import LOGIN_KEY
from home_app.models.user import User
from home_app.models.post import Post
from home_app.models.comment import Comment

@app.route("/wall")
def wall():
    if not LOGIN_KEY in session:
        return redirect("/")
    return render_template("wall.html", posts=Post.get_all_with_comments(), user=User.get_one(session[LOGIN_KEY]))

@app.route("/wall", methods=["POST"])
def create_post():
    if Post.validate(request.form):
        Post.save(request.form)
        return redirect("/wall")
    else:
        return render_template("wall.html", posts=Post.get_all(), user=User.get_one(session[LOGIN_KEY]), post=request.form)

@app.route("/wall/comment", methods=["POST"])
def create_comment():
    Comment.save(request.form)
    return redirect("/wall")
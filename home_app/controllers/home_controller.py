from home_app import app
from home_app.models.user import User
from flask import render_template, redirect, request, session

LOGIN_KEY = "user_id"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if User.validate(request.form):
        session[LOGIN_KEY] = User.save(request.form)
        return redirect("/wall")
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    login_result = User.authenticate(request.form["email"], request.form["password"])
    if login_result:
        session[LOGIN_KEY] = login_result
        return redirect("/wall")
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear();
    return redirect("/")

@app.route("/success")
def success():
    user = User.get_one(session[LOGIN_KEY])
    return f"Welcome, {user.first_name}"


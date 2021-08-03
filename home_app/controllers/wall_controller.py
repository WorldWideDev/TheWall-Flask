# from home_app import app
# from home_app.models.dojo import Dojo
# from home_app.models.ninja import Ninja
# from flask import render_template, redirect, request
# 
# @app.route("/")
# def index():
#     return redirect("/dojos")
# 
# @app.route("/dojos")
# def dojos():
#     return render_template("dojos.html", dojos=Dojo.get_all())
# 
# @app.route("/ninjas")
# def new_ninja():
#     return render_template("new_ninja.html", dojos=Dojo.get_all())
# 
# @app.route("/dojos/create", methods=["POST"])
# def create_dojo():
#     new_dojo = Dojo.save(request.form)
#     return redirect(f"/dojos/{new_dojo.id}")
# 
# 
# @app.route("/ninjas/create", methods=["POST"])
# def create_ninja():
#     new_ninja = Ninja.save(request.form)
#     return redirect(f"/dojos/{new_ninja.dojo_id}")
# 
# @app.route("/dojos/<id>")
# def show_dojo(id):
#     return render_template("dojo.html", dojo=Dojo.get_one(id))

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository
import repositories.post_repository as post_repository
import repositories.thread_repository as thread_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", users = users)

@users_blueprint.route("/users/new_user")
def new_user():
    return render_template("/users/new.html")

@users_blueprint.route("/users/edit/<id>")
def edit_profile(id):
    user = user_repository.select(id)
    return render_template("users/edit.html", user=user)

@users_blueprint.route("/users/<id>", methods=['POST'])
def confirm_edit(id):
    user_name = request.form['user_name']
    sig = request.form['sig']
    avatar_id = request.form['avatar_id']
    user_repository.edit_user(user_name, sig, avatar_id, id)
    return redirect("/users")

@users_blueprint.route("/users", methods=["POST"])
def add_user():
    user_name = request.form["user_name"]
    sig = request.form['sig']
    avatar_id = request.form["avatar_id"]
    admin_status = request.form["admin_status"]
    user = User(user_name, sig, avatar_id, False, admin_status)
    user_repository.create_user(user)
    return redirect("/users")

@users_blueprint.route("/users/<id>")
def show_user(id):
    user = user_repository.select(id)
    posts = post_repository.select_posts_by_user(id)
    threads = thread_repository.select_all()
    return render_template("users/user.html", user = user, posts = posts, threads = threads)
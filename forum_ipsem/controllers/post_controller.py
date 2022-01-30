from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
from models.thread import Thread
from models.post import Post
import repositories.user_repository as user_repository
import repositories.thread_repository as thread_repository
import repositories.post_repository as post_repository

posts_blueprint = Blueprint("posts", __name__)

@posts_blueprint.route("/posts")
def posts():
    posts = post_repository.select_all()
    users = user_repository.select_all()
    return render_template("posts/index.html", posts = posts, users = users)


@posts_blueprint.route("/posts/<id>")
def show(id):
    post = post_repository.select(id)
    users = user_repository.select_all()
    return render_template("posts/post.html", post = post, users = users)
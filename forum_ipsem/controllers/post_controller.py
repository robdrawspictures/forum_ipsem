from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
from models.thread import Thread
from models.post import Post
import repositories.user_repository as user_repository
import repositories.thread_repository as thread_repository
import repositories.post_repository as post_repository
import pdb

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

@posts_blueprint.route("/posts/<id>/edit", methods=['GET'])
def edit_post(id):
    post = post_repository.select(id)
    return render_template("/posts/edit.html", post = post)

@posts_blueprint.route("/posts/<id>/edit", methods=['POST'])
def post_edited(id):
    edit = request.form['post_edit']
    post_repository.edit_post(edit, id)
    post = post_repository.select(id)
    return redirect("/threads/" + str(post.thread_id))

@posts_blueprint.route("/posts/<id>/delete", methods=['POST'])
def post_deleted(id):
    thread = post_repository.select(id)
    # pdb.set_trace()
    post_repository.delete_post(id)
   
    return redirect("/threads/" + str(thread.thread_id))
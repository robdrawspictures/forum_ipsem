from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
from models.thread import Thread
from models.post import Post
import repositories.user_repository as user_repository
import repositories.thread_repository as thread_repository
import repositories.post_repository as post_repository

threads_blueprint = Blueprint("threads", __name__)

@threads_blueprint.route("/threads")
def threads():
    threads = thread_repository.select_all()
    users = user_repository.select_all()
    return render_template("threads/index.html", threads = threads, users = users)


@threads_blueprint.route("/threads/<id>")
def show(id):
    thread = thread_repository.select(id)
    posts = thread_repository.get_posts(id)
    users = user_repository.select_all()
    return render_template("threads/thread.html", thread = thread, posts = posts, users = users)

@threads_blueprint.route("/threads/<id>", methods=['POST'])
def new_post(id):
    user_id = int(request.form['user_id'])
    post_content = request.form['post_content']
    thread_id = id
    new_post = Post(post_content, user_id, thread_id)
    post_repository.create_post(new_post)
    thread = thread_repository.select(id)
    posts = thread_repository.get_posts(id)
    users = user_repository.select_all()
    return render_template("threads/thread.html", thread = thread, posts=posts, users=users)



# Note for future self: You're going to need a find_user_by_name function to
# get around this fine mess you've made, using the creator's name instead of
# their user ID, you absolute plank.
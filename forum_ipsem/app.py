from flask import Flask, render_template

from controllers.post_controller import posts_blueprint
from controllers.thread_controller import threads_blueprint
from controllers.user_controller import users_blueprint
import repositories.user_repository as user_repository
import repositories.post_repository as post_repository
import repositories.thread_repository as thread_repository
import random

app = Flask(__name__)

app.register_blueprint(posts_blueprint)
app.register_blueprint(threads_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    quotes = ["ayy lmao", "the wages of sin are death", "safety not guaranteed", "Stay hydrated. This is a threat"]
    quote = random.choice(quotes)
    users = user_repository.select_all()
    posts = post_repository.select_all()
    threads = thread_repository.select_all()
    return render_template('index.html', quote = quote, users = users, threads = threads, posts = posts)

if __name__ == '__main__':
    app.run(debug=True)
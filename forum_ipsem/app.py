from flask import Flask, render_template

# from controllers.post_controller import posts_blueprint
# from controllers.thread_controller import threads_blueprint
# from controllers.user_controller import users_blueprint

app = Flask(__name__)

# app.register_blueprint(posts_blueprint)
# app.register_blueprint(threads_blueprint)
# app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
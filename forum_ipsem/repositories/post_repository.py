from db.run_sql import run_sql
from models.post import Post
from models.user import User
from models.thread import Thread

def create_post(post):
    sql = "INSERT INTO posts (post_content, user_id, thread_id) VALUES (%s, %s, %s) RETURNING id"
    values = [post.post_content, post.user_id, post.thread_id]
    results = run_sql(sql, values)
    post.post_id = results[0]['id']
    return post

def select(id):
    post = None
    sql = "SELECT * FROM posts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        post = Post(result['post_content'], result['user_id'], result['thread_id'], result['id'] )
    return post

def select_all():
    posts = []
    sql = "SELECT * FROM posts"
    results = run_sql(sql)

    for row in results:
        post = Post(row['post_content'], row['user_id'], row['thread_id'], row['id'])
        posts.append(post)

    return posts

def select_posts_by_user(id):
    posts = []
    sql = "SELECT * FROM posts WHERE user_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        post = Post(row['post_content'], row['user_id'], row['thread_id'], row['id'])
        posts.append(post)

    return posts

def select_posts_by_thread(id):
    posts = []
    sql = "SELECT * FROM posts WHERE thread_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        post = Post(row['post_content'], row['user_id'], row['thread_id'], row['id'])
        posts.append(post)

    return posts

def get_thread_by_post(id):
    sql = "SELECT thread_id WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    return result

def edit_post(edit, id):
    sql = "UPDATE posts SET post_content = %s WHERE id = %s"
    values = [edit, id]
    run_sql(sql, values)

def delete_post(id):
    sql = "DELETE FROM posts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_posts_by_thread(id):
    sql = "DELETE FROM posts WHERE thread_id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all_posts():
    sql = "DELETE FROM posts"
    run_sql(sql)
from db.run_sql import run_sql
from models.post import Post
from models.user import User
from models.thread import Thread

def create_thread(thread):
    sql = "INSERT INTO threads (title, creator, locked) VALUES (%s, %s, %s) RETURNING id"
    values = [thread.title, thread.creator, thread.locked]
    results = run_sql(sql, values)
    thread.thread_id = results[0]['id']
    return thread

def select(id):
    thread = None
    sql = "SELECT * FROM threads WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        thread = Thread(result['title'], result['creator'], result['locked'], result['id'] )
    return thread

def select_all():
    threads = []
    sql = "SELECT * FROM threads"
    results = run_sql(sql)

    for row in results:
        thread = Thread(row['title'], row['creator'], row['locked'], row['id'])
        threads.append(thread)

    return threads

def delete_all_threads():
    sql = "DELETE FROM threads"
    run_sql(sql)

def users(thread):
    users = []
    sql = "SELECT users.* FROM users INNER JOIN posts ON posts.user_id = users.id WHERE thread_id = %s"
    values = [thread.id]
    results = run_sql(sql, values)

    for row in results:
        user = User(row['user_name'], row['sig'], row['avatar_id'], row['account_banned'], row['admin_status'], row['id'])
        users.append(user)
        
    return users

def get_posts(id):
    posts = []
    sql = "SELECT * FROM posts WHERE thread_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        post = Post(row['post_content'], row['user_id'], row['thread_id'], row['id'])
        posts.append(post)

    return posts
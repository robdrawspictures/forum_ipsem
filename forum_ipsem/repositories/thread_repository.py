from db.run_sql import run_sql
from models.post import Post
from models.user import User
from models.thread import Thread

def create_thread(thread):
    sql = "INSERT INTO threads (title, creator) VALUES (%s, %s) RETURNING id"
    values = [thread.title, thread.creator]
    results = run_sql(sql, values)
    thread.thread_id = results[0]['id']
    return thread
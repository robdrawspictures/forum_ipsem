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

def select(id):
    thread = None
    sql = "SELECT * FROM threads WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        thread = Thread(result['title'], result['creator'], result['id'] )
    return thread

def select_all():
    threads = []
    sql = "SELECT * FROM threads"
    results = run_sql(sql)

    for row in results:
        thread = Thread(row['title'], row['creator'], row['id'])
        threads.append(thread)

    return threads

def delete_all_threads():
    sql = "DELETE FROM threads"
    run_sql(sql)
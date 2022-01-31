from db.run_sql import run_sql
from models.post import Post
from models.user import User
from models.thread import Thread

def create_user(user):
    sql = "INSERT INTO users (user_name, avatar_id, admin_status, account_banned) VALUES (%s, %s, %s, %s) RETURNING id"
    values = (user.user_name, user.avatar_id, user.admin_status, user.account_banned)
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return user

def edit_user(user_name, avatar_id, user_id):
    sql = "UPDATE users SET(user_name, avatar_id) = (%s, %s) WHERE id = %s"
    values = [user_name, avatar_id, user_id]
    run_sql(sql, values)

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result['user_name'], result['avatar_id'], result['account_banned'], result['admin_status'], result['id'] )
    return user
    
def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['user_name'], row['avatar_id'], row['account_banned'], row['admin_status'], row['id'])
        users.append(user)

    return users

def ban_user(id):
    sql = "UPDATE users SET account_banned = True WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)
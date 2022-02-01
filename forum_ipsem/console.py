import pdb
from models.post import Post
from models.user import User
from models.thread import Thread

import repositories.post_repository as post_repository
import repositories.user_repository as user_repository
import repositories.thread_repository as thread_repository

user_repository.delete_all()
thread_repository.delete_all_threads()
post_repository.delete_all_posts()

user1 = User("shinji_ikari", "I hate you, dad.", 1)
user_repository.create_user(user1)
user2 = User("rei_ayanami", "...", 2)
user_repository.create_user(user2)
user3 = User("asuka_soryu_langley", "I hate everyone.", 3)
user_repository.create_user(user3)
user4 = User("gendo_ikari", "I hate you, son.", 4, False, True)
user_repository.create_user(user4)

# single_user = user_repository.select(1)
# print(single_user.__dict__)

# user_repository.ban_user(1)

# all_users = user_repository.select_all()
# for user in all_users:
#     print(user.__dict__)

thread1 = Thread("Your Waifu Is Trash", user1.user_name)
thread_repository.create_thread(thread1)
thread2 = Thread("Why Won't My Son Just Get In The Robot", user4.user_name)
thread_repository.create_thread(thread2)

post1 = Post("Die mad about it nerds.", 1, 1)
post_repository.create_post(post1)

post2 = Post("Shinji get in the damn robot.", 4, 1)
post_repository.create_post(post2)

post3 = Post("lol whatever u say virgin", 3, 1)
post_repository.create_post(post3)

post4 = Post("I literally can't even, any more.", 4, 2)
post_repository.create_post(post4)
post5 = Post("Shut up I hate you dad.", 1, 2)
post_repository.create_post(post5)
post6 = Post("I hate that you won't get in the robot tbh", 4, 2)
post_repository.create_post(post6)

post7 = Post("...", 2, 1)
post_repository.create_post(post7)
post8 = Post("...", 2, 2)
post_repository.create_post(post8)

# single_post = post_repository.select(1)
# print(single_post.__dict__)

# all_posts = post_repository.select_all()
# for post in all_posts:
#     print(post.__dict__)

# user_posts = post_repository.select_posts_by_user(2)
# for u_post in user_posts:
#     print(u_post.__dict__)

# thread_posts = post_repository.select_posts_by_thread(2)
# for t_post in thread_posts:
#     print(t_post.__dict__)

# single_thread = thread_repository.select(2)
# print(single_thread.__dict__)

# all_threads = thread_repository.select_all()
# for thread in all_threads:
#     print(thread.__dict__)

post9 = Post('brb running away again for 20 minutes', 1, 2)
post_repository.create_post(post9)
# test1 = post_repository.select(9)

# print(test1.__dict__)

# post_repository.edit_post("brb running away for 10 minutes", 9)
# test2 = post_repository.select(9)

# print(test2.__dict__)

# post_repository.delete_post(7)

pdb.set_trace()
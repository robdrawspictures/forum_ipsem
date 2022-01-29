import pdb
from models.post import Post
from models.user import User
from models.thread import Thread

import repositories.post_repository as post_repository
import repositories.user_repository as user_repository
import repositories.thread_repository as thread_repository

user_repository.delete_all()

user1 = User("shinji_ikari", 1)
user_repository.create_user(user1)
user2 = User("rei_ayanami", 2)
user_repository.create_user(user2)
user3 = User("asuka_soryu_langley", 3)
user_repository.create_user(user3)
user4 = User("gendo_ikari", 4, False, True)
user_repository.create_user(user4)

# single_user = user_repository.select(1)
# print(single_user.__dict__)

# user_repository.ban_user(1)

# all_users = user_repository.select_all()
# for user in all_users:
#     print(user.__dict__)

thread1 = Thread("Your Waifu Is Trash", user1.user_name)
thread_repository.create_thread(thread1)
thread2 = Thread("Why Won't My Son Just Get In The Fucking Robot", user4.user_name)
thread_repository.create_thread(thread2)

post1 = Post("Die mad about it nerds.", 1, 1)
post_repository.create_post(post1)

post2 = Post("Shinji get in the fucking robot.", 4, 1)
post_repository.create_post(post2)

post3 = Post("cope harder incel lmao", 3, 1)
post_repository.create_post(post3)

post4 = Post("I literally can't even, any more.", 4, 2)
post_repository.create_post(post4)
post5 = Post("Shut up I hate you dad.", 1, 2)
post_repository.create_post(post5)
post6 = Post("I hate that you won't get in the fucking robot tbh", 4, 2)
post_repository.create_post(post6)

single_post = post_repository.select(1)
print(single_post.__dict__)

all_posts = post_repository.select_all()
for post in all_posts:
    print(post.__dict__)

pdb.set_trace()
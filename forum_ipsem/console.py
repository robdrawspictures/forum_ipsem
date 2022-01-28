import pdb
from models.post import Post
from models.user import User
from models.thread import Thread

# import repositories.post_repository as post_repository
import repositories.user_repository as user_repository
# import repositories.thread_repository as thread_repository

user_repository.delete_all()

user1 = User("shinji_ikari", 1)
user_repository.create_user(user1)
user2 = User("rei_ayanami", 2)
user_repository.create_user(user2)
user3 = User("asuka_soryu_langley", 3)
user_repository.create_user(user3)
user4 = User("gendo_ikari", 4, False, True)
user_repository.create_user(user4)

single_user = user_repository.select(1)
print(single_user.__dict__)

user_repository.ban_user(1)

all_users = user_repository.select_all()
for user in all_users:
    print(user.__dict__)



pdb.set_trace()
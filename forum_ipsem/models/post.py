class Post:
    def __init__(self, post_content, user_id, thread_id, post_id = None):
        self.post_id = post_id
        self.post_content = post_content
        self.user_id = user_id
        self.thread_id = thread_id
class Thread:
    def __init__(self, title, creator, locked = False, thread_id = None):
        self.title = title
        self.creator = creator
        self.locked = locked
        self.thread_id = thread_id
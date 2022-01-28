class User:
    def __init__(self, user_name, avatar_id = None, account_banned = False, admin_status = False, user_id = None):
        self.user_name = user_name
        self.avatar_id = avatar_id
        self.account_banned = account_banned
        self.admin_status = admin_status
        self.user_id = user_id
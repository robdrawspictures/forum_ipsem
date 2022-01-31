class User:
    def __init__(self, user_name, sig, avatar_id = None, account_banned = False, admin_status = False, user_id = None):
        self.user_name = user_name
        self.sig = sig
        self.avatar_id = avatar_id
        self.account_banned = account_banned
        self.admin_status = admin_status
        self.user_id = user_id

    def ban_user(self):
        self.account_banned = True

    def grant_admin(self, id):
        self.admin_status = True 
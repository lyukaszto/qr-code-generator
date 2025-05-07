class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise ValueError("User already exists.")
        self.users[username] = password

    def authenticate_user(self, username, password):
        if username not in self.users:
            return False
        return self.users[username] == password

    def list_users(self):
        return list(self.users.keys())
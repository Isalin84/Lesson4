from user import User

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users = []

    def add_user(self, user):
        self._users.append(user)
        print(f"User {user.get_name()} added successfully.")

    def remove_user(self, user_id):
        self._users = [user for user in self._users if user.get_user_id() != user_id]
        print(f"User with ID {user_id} removed successfully.")

    def list_users(self):
        print("List of Users:")
        for user in self._users:
            print(user)

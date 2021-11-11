from Model.users import Users


class UserList:

    def __init__(self):
        self.user_list = []

    # Adds a new user to the user list store
    def add(self, user: Users):
        if self.get_user_by_username(user.get_username()):
            raise KeyError(f"Invalid input, Username {user.get_username()} already exist")

        self.user_list.append(user)

    # View all users within the user list
    def view(self):
        for user in self.user_list:
            print(user.get_username())

    # Searches for a user based on the firstname data
    def search(self, firstname):
        return [user for user in self.user_list if user.get_firstname() == firstname]

    # removes a user object from the user list store.
    def remove(self, user):
        # returns a statement if two or more user exist with the same firstname
        if self.is_duplicate(user, 'firstname'):
            print('Two or more users with the same firstname')
            return

        for i in range(len(self.user_list)):
            users = self.user_list[i]
            if users.get_firstname() == user.get_firstname():
                return self.user_list.pop(i)

    # Gets the total number of users in the user list
    def count(self):
        return len(self.user_list)

    # Gets user by username
    def get_user_by_username(self, username):
        for user in self.user_list:
            if user.get_username() == username:
                return user

    # Checks if username is duplicate
    def is_duplicate(self, user: Users, data_input):
        user = self.search(getattr(user, data_input))
        if len(user) > 1:
            return True
        return False


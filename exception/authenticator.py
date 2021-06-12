from auth_exceptions import UserNameAlreadyExists, PasswordTooShort, InvalidUsername, \
    InvalidPassword
from user import User


class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, user_name, password):
        if user_name in self.users:
            raise UserNameAlreadyExists(user_name)
        if len(password) < 7:
            raise PasswordTooShort(user_name)
        self.users[user_name] = User(user_name, password)

    def login(self, user_name, password):
        try:
            user = self.users[user_name]
        except KeyError as e:
            raise InvalidUsername(user_name)
        if not user.check_password(password):
            raise InvalidPassword(user_name, user)
        user.is_logged_in = True
        return True


authenticator = Authenticator()

if __name__ == '__main__':
    authenticator.add_user("shashank", "abc12345")
    print(authenticator.login("shashank", "abc12345"))
    print("completed")
class AuthException(Exception):
    def __init__(self, user_name, user=None):
        super().__init__(user_name, user)
        self.user_name = user_name
        self.user = user


class UserNameAlreadyExists(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass
import hashlib


class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = self._encrypt(password)
        self.is_logged_in = False

    def _encrypt(self, password):
        hash_string = self.user_name + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        encrypted = self._encrypt(password)
        return encrypted == self.password

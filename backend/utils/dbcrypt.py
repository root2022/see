#coding=utf-8
from cryptography.fernet import Fernet

class prpcrypt:

    key = 'P30cMRRBa9kF3YNYpeKNmlUquLsX6ssOuBdy4yZe8wU='

    @classmethod
    def encrypt(cls, password):
        f = Fernet(cls.key)
        passwd_encode = password.encode()
        token = f.encrypt(passwd_encode)
        return token.decode()

    @classmethod
    def decrypt(cls, password):
        f = Fernet(cls.key)
        passwd_encode = password.encode()
        token = f.decrypt(passwd_encode)
        return token.decode()

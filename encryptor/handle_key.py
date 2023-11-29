from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import os


class AESManager:
    def __init__(self, password: bytes) -> None:
        self.key = self.derive_key(password)

    def derive_key(self, password: bytes) -> bytes:
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            length=32,
            salt=salt,
            backend=default_backend()
        )
        key = kdf.derive(password)
        return key

    def save_key_to_file(self, key_file):
        with open(key_file, 'wb') as f:
            f.write(self.key)

    def load_key_from_file(self, key_file):
        with open(key_file, 'rb') as f:
            self.key = f.read()

    def delete_key_file(self, key_file):
        os.remove(key_file)
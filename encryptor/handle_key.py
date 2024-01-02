from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

class AESManager:

    def save_key_to_file(self, key_file):
        
        while True:
            g_input = input('Lütfen 16 karakterlik anahtarı giriniz: ')
            if len(g_input)==16:
                break
            else:
                print(f"{len(g_input)} karakter girdiniz. Tekrar deneyin\n")
        self.key = bytes(g_input, 'utf-8')

        with open(key_file, 'wb') as f:
            f.write(self.key)

    def load_key_from_file(self, key_file):
        with open(key_file, 'rb') as f:
            self.key = f.read()

    def delete_key_file(self, key_file):
        os.remove(key_file)
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from .handle_key import AESManager
import os


class FileEncryptor:
    def __init__(self, aes_manager: AESManager) -> None:
        self.aes_manager = aes_manager

    def encrypt_file(self, file_path: str, output_path: str) -> bool:
        try:
            with open(file_path, 'rb') as f:
                file_content = f.read()

            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(self.aes_manager.key), modes.CFB(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(file_content) + encryptor.finalize()

            with open(output_path, 'wb') as f:
                f.write(iv + ciphertext)

            print(f"File encrypted and saved to {output_path}")
            return True
        except Exception as e:
            print(f"Encryption error: {e}")
            return False

    def decrypt_file(self, encrypted_file_path: str, output_path: str) -> bool:
        try:
            with open(encrypted_file_path, 'rb') as f:
                data = f.read()

            iv = data[:16]
            ciphertext = data[16:]

            cipher = Cipher(algorithms.AES(self.aes_manager.key), modes.CFB(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_content = decryptor.update(ciphertext) + decryptor.finalize()

            with open(output_path, 'wb') as f:
                f.write(decrypted_content)

            print(f"File decrypted and saved to {output_path}")
            return True
        except Exception as e:
            print(f"Decryption error: {e}")
            return False

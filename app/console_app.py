import argparse
import os
import paramiko
from encryptor import FileEncryptor
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes


class Application():

    def __init__(self) -> None:
        self.home_directory = ""
        self.ssh_directory = ""
        self.public_key_path = ""
        self.private_key_path = ""
        self.key: paramiko.RSAKey = None
        pass

    def Generate_ssh_key_for_applicaiton(self):
        self.home_directory = os.path.expanduser("~")

        self.ssh_directory = os.path.join(self.home_directory, '.ssh')

        if not os.path.exists(self.ssh_directory):
            os.makedirs(self.ssh_directory)
            print(f'"{self.ssh_directory}" klasörü oluşturuldu.')

        self.private_key_path = os.path.join(self.ssh_directory, 'encryption')
        self.public_key_path = os.path.join(self.ssh_directory, 'encryption.pub')
        if not os.path.exists(self.private_key_path) and not os.path.exists(self.public_key_path):
            self.private_key = RSA.generate(2048)
            self.public_key = self.private_key.public_key()
            private_key_path = os.path.join(self.ssh_directory, 'encryption')
            with open(private_key_path, 'w') as private_key_file:
                private_key_file.write(str(self.private_key))
            print(f'Özel anahtar dosyası oluşturuldu: {private_key_path}')

            public_key_path = os.path.join(self.ssh_directory, 'encryption.pub')
            with open(public_key_path, 'w') as public_key_file:
                public_key_file.write(str(self.public_key))
            print(f'Genel anahtar dosyası oluşturuldu: {public_key_path}')
        else:
            pass


    def RunApplication(self):

        self.Generate_ssh_key_for_applicaiton()
        args = self.parser.parse_args()

        if self.public_key is not None and self.private_key is not None:
            private_key_bytes = self.private_key
            public_key_bytes = self.public_key
            fileEncryptor = FileEncryptor(
                key=public_key_bytes, initializer=private_key_bytes
            )

            if args.command == "encrypt":
                print(f"The program starting encryption for {args.file_path}")
                fileEncryptor.EncryptFile(args.file_path)
            elif args.command == "decrypt":
                fileEncryptor.DecryptFile(args.file_path)
                print(f"The program starting decryption for {args.file_path}")


    def ConfigureApplication(self):
        self.parser = argparse.ArgumentParser(description="Image Encrypt Application")
        self.parser.add_argument('--verbose', '-v', action='store_true')

        self.subparsers = self.parser.add_subparsers(dest="command", help="Commands of the encryptor!")

        encrypt_parser = self.subparsers.add_parser("encrypt", help="Encrypt image file")
        encrypt_parser.add_argument("file_path", help="File path to encrypt")

        decrypt_parser = self.subparsers.add_parser("decrypt", help="Decrypt encrypted file")
        decrypt_parser.add_argument("file_path", help="File path to decrypt")

        pass

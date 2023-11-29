import argparse
import os
import paramiko
from encryptor import FileEncryptor
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

from encryptor.handle_key import AESManager


class Application():

    def __init__(self) -> None:
        self.home_directory = os.path.expanduser("~")
        self.ssh_directory = os.path.join(self.home_directory, ".ssh")
        self.private_key_file_path = os.path.join(self.ssh_directory, "encryption_key_private.pem")
        self.key = None
        pass

    def Generate_ssh_key_for_applicaiton(self):
        self.key_handler = AESManager(b'1234')
        if os.path.exists(self.private_key_file_path):
            self.key_handler.load_key_from_file(self.private_key_file_path)
        else:
            self.key_handler.derive_key(b'1234')
            self.key_handler.save_key_to_file(self.private_key_file_path)
 
    def RunApplication(self):

        self.Generate_ssh_key_for_applicaiton()
        args = self.parser.parse_args()
        self.file_encryptor = FileEncryptor(self.key_handler)
        if args.command == "generate_key": 
            print("generating encryption key")
            self.Generate_ssh_key_for_applicaiton()
        elif args.command == "delete_key":
            print("deleting encryption key")
            self.key_handler.delete_key_file(self.private_key_file_path)
        elif args.command == "encrypt":
            print(f"The program starting encryption for {args.file_path}")
            self.file_encryptor.encrypt_file(args.file_path, "test.txt")
        elif args.command == "decrypt":
            print(f"The program starting decryption for {args.file_path}")
            self.file_encryptor.decrypt_file(args.file_path, "wallpaper2.png")
    
    def ConfigureApplication(self):
        self.parser = argparse.ArgumentParser(description="Image Encrypt Application")
        self.parser.add_argument('--verbose', '-v', action='store_true')

        self.subparsers = self.parser.add_subparsers(dest="command", help="Commands of the encryptor!")

        
        generate_key_parser = self.subparsers.add_parser("generate_key", help="To Generate keys")
        delete_key_parser = self.subparsers.add_parser("delete_key", help="To Delete keys")

        encrypt_parser = self.subparsers.add_parser("encrypt", help="Encrypt image file")
        encrypt_parser.add_argument("file_path", help="File path to encrypt")

        decrypt_parser = self.subparsers.add_parser("decrypt", help="Decrypt encrypted file")
        decrypt_parser.add_argument("file_path", help="File path to decrypt")

        pass

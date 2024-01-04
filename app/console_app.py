import argparse
import os
import sys
import paramiko
from encryptor import FileEncryptor
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

from encryptor.handle_key import AESManager


class Application():

    def __init__(self) -> None:
        self.home_directory = os.path.dirname(sys.modules['__main__'].__file__)
        self.ssh_directory = os.path.join(self.home_directory, ".ssh")
        self.private_key_file_path = os.path.join(self.ssh_directory, "encryption_key_private.pem")
        self.key = None
        print(os.path.exists(self.private_key_file_path))
        pass

    def Generate_ssh_key_for_applicaiton(self):
        #oluşturulan anahtar .ssh klasöründe tutuluyor.
        #eğer klasör yoksa projenin içine oluşturuluyor
        self.key_handler = AESManager()
        if not os.path.exists(self.ssh_directory):
            os.makedirs(".ssh")
            print(".ssh folder created")
        if os.path.exists(self.private_key_file_path):
            #dizinde bir anahtar varsa key_handler değişkenine atıyoruz
            self.key_handler.load_key_from_file(self.private_key_file_path)
        else:
            #eğer dizinde bir anahtar yoksa save_key_to_file fonksiyonu ile
            #kullanıcıdan yeni bir anahtar alıyoruz
            self.key_handler.save_key_to_file(self.private_key_file_path)
            print("cryption key created on .ssh folder")
 
    def RunApplication(self):
        #argümanların tanımlandığı fonksiyondur
        self.Generate_ssh_key_for_applicaiton()
        args = self.parser.parse_args()
        self.file_encryptor = FileEncryptor(self.key_handler)
        if args.command == "generate_key":
            #generate_key komutu ile kullanıcıdan alınan veri ile yeni bir
            #anahtar oluşturuyoruz  
            print("generating encryption key")
            self.Generate_ssh_key_for_applicaiton()
        elif args.command == "delete_key":
            #delete_key komutu ile varolan anahtarı siliyoruz
            print("deleting encryption key")
            self.key_handler.delete_key_file(self.private_key_file_path)
        elif args.command == "encrypt":
            #encrypt komutu ile eğer bir anahtar varsa argüman olarak verilen dosyayı
            #şifreliyoruz. eğer anahtar yoksa kullanıcıdan yeni bir anahtar alıp
            #şifreleme işlemi yapıyoruz
            print(f"The program starting encryption for {args.file_path}")
            self.file_encryptor.encrypt_file(args.file_path, "en_"+str(os.path.basename(args.file_path)))
        elif args.command == "decrypt":
            #decrypt komutu ile eğer bir anahtar varsa argüman olarak verilen dosyayı
            #deşifreliyoruz. eğer anahtar yoksa kullanıcıdan yeni bir anahtar alıp
            #deşifreleme işlemi yapıyoruz
            print(f"The program starting decryption for {args.file_path}")
            self.file_encryptor.decrypt_file(args.file_path, "de"+os.path.basename(args.file_path)[2:])
    
    def ConfigureApplication(self):
        self.parser = argparse.ArgumentParser(description="Image Encrypt Application")
        self.parser.add_argument('--verbose', '-v', action='store_true')

        self.subparsers = self.parser.add_subparsers(dest="command", help="Commands of the encryptor!")

        #argümanların tanımlandığı fonksiyon
        generate_key_parser = self.subparsers.add_parser("generate_key", help="To Generate keys")
        delete_key_parser = self.subparsers.add_parser("delete_key", help="To Delete keys")

        encrypt_parser = self.subparsers.add_parser("encrypt", help="Encrypt image file")
        encrypt_parser.add_argument("file_path", help="File path to encrypt")

        decrypt_parser = self.subparsers.add_parser("decrypt", help="Decrypt encrypted file")
        decrypt_parser.add_argument("file_path", help="File path to decrypt")

        pass

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class FileEncryptor():
    __key: bytes
    __initalizationVector: bytes
    __cipher: any

    def __init__(self, key, initializer) -> None:
        self.__key = key
        self.__initalizationVector = initializer
        self.__cipher = AES.new(self.__key, AES.MODE_CBC, self.__initalizationVector)
        print(self.__key)
        print(self.__initalizationVector)
        print(self.__key)
        print(self.__initalizationVector)

    def EncryptTest(self, file_path):
        print("encrypt script running.")

    def EncryptFile(self, file_path) -> bool:
        try:
            with open(file_path, 'rb') as f:
                file_content = f.read()
            file_content_padded = file_content + b' ' * (16 - len(file_content) % 16)
            encryptedFile = self.__cipher.encrypt(file_content_padded)
            with open(encryptedFile, 'wb') as f:
                f.write(encryptedFile)
        except Exception as e:
            print(e)
            return False
        print("file encrypted..")
        return True

    def DecryptFileTest(self, file_path, original_file):
        print("Decrypt file running. ")

    def DecryptFile(self, file_path, original_file) -> bool:
        try:
            with open(file_path, 'rb') as f:
                file_content = f.read()
            decrypted_file_content_padded = self.__cipher.decrypt(file_content)
            decrypted_file_content = decrypted_file_content_padded.rstrip(b' ')
            decrypted_file_name = original_file
            with open(decrypted_file_name, 'wb') as f:
                f.write(decrypted_file_content)
            return True
        except:
            print("file cannot decrypted")
            return False

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

class AESManager:
    #bu class'da anahtar oluşturma ve varolan anahtarı silme işlemlerini yapıyoruz
    def save_key_to_file(self, key_file):
        #kullanıcıdan 16 karakterlik bir anahtar alana kadar bu döngü devam eder
        while True:
            g_input = input('Lütfen 16 karakterlik anahtarı giriniz: ')
            if len(g_input)==16:
                #16 karakter kontrolünden geçtikten sonra döngü bitirilir
                break
            else:
                #16 karakterden farklı bir değer girildiğinde kullanıcı uyarılır ve 
                #tekrar anahtar girmesi istenir.
                print(f"{len(g_input)} karakter girdiniz. Tekrar deneyin\n")
        self.key = bytes(g_input, 'utf-8')

        #kullanıcının girdiği anahtar belirtilen dizine kaydedilir.
        with open(key_file, 'wb') as f:
            f.write(self.key)

    def load_key_from_file(self, key_file):
        #key_file dizininde eğer bir anahtar varsa key değişkenine atayan fonksiyon
        with open(key_file, 'rb') as f:
            self.key = f.read()

    def delete_key_file(self, key_file):
        #key_file dizinindeki anahtarı sildiğimiz fonksiyon
        os.remove(key_file)
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from .handle_key import AESManager
import os

class FileEncryptor:
    #şifreleme ve deşifreleme işleminin yapıldığı class
    def __init__(self, aes_manager: AESManager) -> None:
        #class oluşturulduğunda şifreleme ve deşifrelemede kullanacağımız
        #initial vector'ümüzü 16 bytelık 0 olacak şekilde tanımlıyoruz
        self.aes_manager = aes_manager
        self.init_vector = b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'

    def encrypt_file(self, file_path: str, output_path: str) -> bool:
        #şifreleme işleminin yapıldığı fonksiyon
        try:
            with open(file_path, 'rb') as f:
                #file_path dizininde bulunan şifrelenecek dosyayı açıp
                #file_content değişkenine atıyoruz
                file_content = f.read()

            cipher = Cipher(algorithms.AES(self.aes_manager.key), modes.CFB(self.init_vector), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(file_content) + encryptor.finalize()

            #oluşturulan key ile şifreleme işlemini yapıp dosyaya şifrelenmiş veriyi yazıyoruz
            
            with open(output_path, 'wb') as f:
                f.write(self.init_vector + ciphertext)

            print(f"File encrypted and saved to {output_path}")
            return True
        except Exception as e:
            print(f"Encryption error: {e}")
            return False

    def decrypt_file(self, encrypted_file_path: str, output_path: str) -> bool:
        #deşifreleme işleminin yapıldığı fonksiyon
        try:
            with open(encrypted_file_path, 'rb') as f:
                #file_path dizininde bulunan deşifrelenecek dosyayı açıp
                #data değişkenine atıyoruz
                data = f.read()

            #data verisinin ilk 16 karakteri init vector olduğu için 16 karakterden sonraki datayı
            #ciphertext değişkenine atıyoruz. burası şifrelenecek kısım.
            ciphertext = data[16:]

            cipher = Cipher(algorithms.AES(self.aes_manager.key), modes.CFB(self.init_vector), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_content = decryptor.update(ciphertext) + decryptor.finalize()
            
            #oluşturulan key ile deşifreleme işlemini yapıp dosyaya deşifrelenmiş veriyi yazıyoruz
            
            with open(output_path, 'wb') as f:
                f.write(decrypted_content)

            print(f"File decrypted and saved to {output_path}")
            return True
        except Exception as e:
            print(f"Decryption error: {e}")
            return False

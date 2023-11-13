# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
from encryptor import FileEncryptor
from app import Application


# Şifrelenecek dosyanın adı
# dosya_adı = "wallpaper.png"

# # Rastgele bir 128-bit anahtar oluşturun
# anahtar = get_random_bytes(16)

# # IV (Initialization Vector) oluşturun (AES-CBC modu için gereklidir)
# iv = get_random_bytes(16)

# # AES şifreleme nesnesini oluşturun
# cipher = AES.new(anahtar, AES.MODE_CBC, iv)

# # Dosyayı okuyun
# with open(dosya_adı, 'rb') as f:
#     dosya_icerigi = f.read()

# # Dosyayı şifreleyin
# dosya_icerigi_paddeden = dosya_icerigi + b' ' * (16 - len(dosya_icerigi) % 16)  # PKCS7 padding
# sifrelenmis_dosya = cipher.encrypt(dosya_icerigi_paddeden)

# # Şifrelenmiş dosyayı kaydedin
# sifrelenmis_dosya_adı = "sifrelenmis_resim.jpg"
# with open(sifrelenmis_dosya_adı, 'wb') as f:
#     print(sifrelenmis_dosya)
#     f.write(sifrelenmis_dosya)


# print("Dosya şifrelendi ve kaydedildi:", sifrelenmis_dosya_adı)

# # Şifre çözme örneği
# # Aynı anahtar ve IV ile şifreyi çözmek için
# decipher = AES.new(anahtar, AES.MODE_CBC, iv)
# cozulmus_dosya_paddeden = decipher.decrypt(sifrelenmis_dosya)
# cozulmus_dosya = cozulmus_dosya_paddeden.rstrip(b' ')  # Padding'i kaldır

# # Şifresi çözülen dosyayı kaydedin
# cozulmus_dosya_adı = "cozulmus_resim.jpg"
# with open(cozulmus_dosya_adı, 'wb') as f:
#     f.write(cozulmus_dosya)

# print("Dosya çözüldü ve kaydedildi:", cozulmus_dosya_adı)
def main():
    app = Application()
    app.ConfigureApplication()
    app.RunApplication()


if __name__ == '__main__':
    main()

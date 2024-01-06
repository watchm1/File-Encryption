from encryptor import FileEncryptor
from app import Application
# uygulamanin configure edildigi ve baslatildigi fonksiyon

def main():
    app = Application()
    app.ConfigureApplication()
    app.RunApplication()

if __name__ == '__main__':
    main()
